__author__ = 'danieloram'

import math

#return a list of all primes <= n   O(n^2)
def find_primes(n):
    for i in range(1,n+1):
        if is_prime(i):
            print(i)

#return boolean determined on whether n is prime - not very efficient test
#updated to only test factors up to the square(n)
def is_prime(n):
    if n >=3:
        for i in range(2,n):    #all values from 2 to n-1
            if n%i==0:
                return False
    else:
        return False
    return True

def is_prime_recursive(n):
    if n%(int(n/2))==0:
        return False
    return True

#start at 1 and multiply to see if n is reached, if not - increment and keep iterating until sqrt(n) is reached
#TODO: finish this method
def r_prime(n,r=1):
    return None





find_primes(int(input("Enter an Integer number: ")))