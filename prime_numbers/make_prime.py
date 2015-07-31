__author__ = 'danieloram'

#return a list of all primes <= n
def find_primes(n):
    for i in range(n+1):
        if is_prime(i):
            print(i)

#return boolean deternimed on whether n is prime - not very efficient test
def is_prime(n):
    for i in range(2,n):    #all values from 2 to n-1
        if n%i==0:
            return False
    return True


find_primes(int(input("Enter an Integer number: ")))