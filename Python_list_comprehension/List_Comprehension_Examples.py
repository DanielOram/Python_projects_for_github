__author__ = 'danieloram'


#create a list with string representations for each element's index position
seq = [str(x) for x in range(10)]
#=>['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#create a list of squares 
seq2 = [x*x for x in range(10)]
#=>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#delete elements of a list based on a condition
seq3 = [x for x in range(10) if not x % 2]
#=>[0, 2, 4, 6, 8]

#create a list of primes. the logic is to remove the primes then 'inverse' the list
seq4 = [x for x in range(2, 20) if x not in [j for i in range(2, 10) for j in range(i*2, 20, i)]] 

#split a string into a list of tuples of string,index pairs. could be done more efficiently??
unsplit = "This is a string literal or a sequence of chars followed by a null terminating char"
seq5 = zip([x for x in unsplit.split()],range(len(unsplit.split())))

#split a string into a list of lists including the word and length.
unsplit = "This is a string literal or a sequence of chars followed by a null terminating char"
seq6 = [[x,len(x)] for x in unsplit.split()]

#create a dictionary of strings for keys and lengths for values
unsplit = "This is a string literal or a sequence of chars followed by a null terminating char"
seq7 = {x: len(x) for x in unsplit.split()}

#lambda expression with list comphension to quicker create a list a 'b' list elements all with 'a' numbered elements
lam = lambda a,b: [[x for x in range(a)] for x in range(b)]
print(lam(3,10)) #=> [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

#lambda expression to create a list with a random number of list elements with a random number of elements
from random import randint
r_lam = lambda a,b: [[x for x in range(randint(1,a))] for x in range(randint(1,b))]
print(r_lam(5,5)) #=> [[0, 1, 2], [0], [0, 1, 2]]

#find the max element of each sublist and return the resulting list
t = [[0, 1, 2], [0, 1, 2, 3], [0, 1], [0, 1, 2, 3, 4]]
fill = lambda lists: [max(e) for e in lists]
print(fill(t))

#generate a 2d list with a random number of lists each with random elements each unqiue.
from random import randint
#generate random input for this example
randomize = lambda a,b: [list(set([randint(0,9) for x in range(randint(1,a))])) for x in range(b)]

#compress a list function
compf = lambda x: [j for i in x for j in i]

#compress a 2D list into a single list
compress_to_unique = lambda x: list(set([j for i in x for j in i]))
fill = lambda lists: [[f for f in compress_to_unique(lists) if not f in e] for e in lists]
r = randomize(6,10)

print(r)
print(fill(r))

#generate a 2d list with a random number of lists each with random elements each unqiue - in one line
#generate random input
from random import randint
randomize = lambda a,b: [list(set([randint(0,9) for x in range(randint(1,a))])) for x in range(b)]

fill_one_liner = lambda lists: [[e for e in list(set([j for i in lists for j in i])) if not e in a_list] for a_list in lists]
print(fill_one_liner(randomize(5,5)))
