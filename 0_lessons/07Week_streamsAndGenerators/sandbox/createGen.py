def createGenerator():
  mylist = range(3)
  for i in mylist:
  # find the square of the value as needed
    yield i*i
# end of createGenerator()

# Initiation: create a generator
myGenerator = createGenerator()
# Where is this generator in memory?
print(myGenerator)
for i in myGenerator:
  print("\t 1: myGenerator: ",i)

for i in myGenerator:
  print("\t 2: myGenerator: ",i)

