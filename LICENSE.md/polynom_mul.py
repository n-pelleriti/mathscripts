class polynom:
    def __init__(self, coeff_list):
        coeff_list = list(filter(lambda x: x[0] != 0, coeff_list))
        self.coeff_list = sorted(coeff_list, key = lambda x: x[1], reverse=True)
    
    def __add__(self, p2):
        result = []
        # find biggest coeff 
        degree = max(self.coeff_list[0][1], p2.coeff_list[0][1])
        for i in range(degree + 1, -1 , -1):
            coeff = next((x for x in self.coeff_list if x[1] == i), [0])[0] + next((x for x in p2.coeff_list if x[1] == i), [0])[0]
            result = result + [(coeff, i)]
        return polynom(result)
    def __str__(self):
        result = ""
        for summand in self.coeff_list:
            sign = "+ " if summand[0] > 0 else "- "
            result = result + sign +str(abs(summand[0])) + "x**" + str(summand[1]) + " "
        return result if result[0] == "-" else result[2:]
    def __mul__(self, p2):
        result = polynom([(1,0)])
        for summand in self.coeff_list:
            for summand2 in p2.coeff_list:
                result = result + polynom([(summand[0]*summand2[0], summand[1] + summand2[1])])
        return result + polynom([(-1, 0)])

# some example
P1 = polynom([(1,1), (2,2), (3,3), (4,0)])
P2 = polynom([(-1,2), (11, 3), (2, 1), (3, 0)])
print("( " +str(P1)+ " ) * ( " + str(P2) + " )")
print(P1 * P2)