#!/usr/bin/env python3
def combinations(n,seq):
    if n == 0: # base case to know when to stop
        yield ()
    elif len(seq) == 0: # another base case to know when to stop
        pass
    else:
        first = seq[0] # first char in the sequence
#        print("  first :",first)
        rest = seq[1:] # All chars after the first
#        print("    rest :",rest)
        # make a recursive call to self
        for a in combinations(n, rest):
#            print("  _for n:",a)
            #print("\t Yielding the value ...")
            yield a #add this to data structure in memory
        # make another recursive call to self, reduce the n
        for a in combinations(n-1, rest):
#            print("  _for n-1",a)

            yield (first,) + a
#end of combinations()

def n_choose_k_Count(n,k):
    """ function to determine the length of the n choose k list."""
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
# end of n_choose_k_Count()


import math


s_str = "ATGC" # main set (n)
k = 2 # choose this many of them (k)

print("\t Program to show all sets of n\n\t things from which k of them have been chosen")
print("\t Start Program :", len(s_str), "choose",k,"from a string : <<",s_str,">>")

print("\t Number of elements in list: ",n_choose_k_Count(len(s_str), k))

myCombination = combinations(k, s_str)
print("\n\t My type is :",type(myCombination)) # Is this a generator type?
print("\t Possible combinations of elements chosen this way ")
for i in myCombination: #iterator
    print("\t  ",i) # engage the generator function for operation
print("\t End Program")
