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

# Code to call the functions above is here ...

print("\t End Program")
