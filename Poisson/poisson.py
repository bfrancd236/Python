from math import pow, factorial



def poisson(x, lam):
    return round(pow(2.71828,-lam) * pow(lam,x) / factorial(x), 4)

print("Previsão de:",poisson(3,2)*100,"%")