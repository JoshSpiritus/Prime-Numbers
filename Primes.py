import math
def Is_n_prime(n):
    if n ==1:
        return False
    if n == 2:
        return True
    if n % 2 == 0 and n > 2:
        return False
    '''Calculate the maximum divisor to test be used in for loop,
    it will be squareroot of the maximum value in range'''
    max_div = int(math.floor(math.sqrt(n)))
    for d in range(3, max_div + 1, 2):
        if n % d == 0:
            return False
    return True
for n in range(1,100):    #Checking Primes in a Range 1-100
    if Is_n_prime(n) is True:
        print n, " is a Prime Number"
    else:
        print n, " is not a Prime Number"
#To check one number uncomment the below line
#print Is_n_prime(17)