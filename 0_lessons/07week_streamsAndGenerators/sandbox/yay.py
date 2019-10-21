# A simple generator function
def my_gen():
   n = 1
   print("\t A: Output n :", n)
   # Generator function containing yield statements
   yield n
   print("\t A: Output after yielding n :",n,"\n____")

   n += 1
   print("\t B: Output n :",n)
   yield n
   print("\t B: Output after yielding n :",n,"\n____")

   n += 1
   print("\t C: Output n :",n)
   yield n
   print("\t C: Output after yielding n :",n,"\n____")

   print(" ")

#end of my_gen()

# Calls return an object but does not start execution immediately.
a = my_gen() # generator function
print(" a = ",a)
next(a)# first output
next(a)# second output
next(a)# last output

# Using for loop
print( "Use the loop.\n______")
for i in my_gen():
   print(i)
