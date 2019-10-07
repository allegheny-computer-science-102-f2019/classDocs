l_list = ["Apples", "Oranges", "Apricots", "Avocado", "Ananas (pineapple)", "Asparagus"]
names = (line[:] for line in l_list) # create a generator
print(" Name variable is: ",names) # generator function, no data added just yet
type(names) # <class 'generator'>
for i in names:print("\t First round :",i)
print("\t Let's try that again! ")
for i in names:print("\t Second round :",i) #... ?
