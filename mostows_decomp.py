"""
Here we use sympy to calculate the mostow's decomposition of a regular complex matrix
"""
import sympy as sp

def mostow_dec(Z):
    """
    This function computes the Mostow's decomposition of matrix, i.e.
    
    Z = W*exp(iK)*exp(S)
    
    where W,K,S are C^{n x n} matrices.
    
    Arguments:
        Z : a square, non singular matrix with complex entries
    Returns:
        W,K,S: Matrices of the Mostow's decompostion 
    """
    try:
        # calculate determinate to check for singularity and square matrix
        d = sp.det(Z)
        # throw an exception if Z is singular
        if d == 0:
            raise ValueError
        # calculate W,K,S accordingly for the Mostow's decomposition 
        A = Z*Z
        A_inv = A.inv()
        K = 1/(0-2j)*(A**(0.5)*(A**(-0.5)*(A_inv)*(A)**(-0.5))**0.5*A_inv**0.5).log()
        X = ((0-1j)*K).exp()*A*((0-1j)*K).exp()
        S = 0.5*X.log()
        W = Z*((0-1j)*K).exp()*(-1*S).exp()
        return W,K,S
    # catch the error that Z is singular or square
    except ValueError as e2:
        print("Mostow's decomposition requires a non singular, square matrix")

# some example 
M = sp.Matrix([[-1,1,5],[0,42,12]])
W,K,S = mostow_dec(M)
print(W,K,S)
print(W*((0+1j)*K).exp()*S.exp())