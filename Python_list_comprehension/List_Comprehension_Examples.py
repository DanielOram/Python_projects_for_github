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



