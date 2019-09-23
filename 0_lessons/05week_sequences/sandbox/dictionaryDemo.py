# Date: 23 Sept 2019
# Dictionary Demo by OBC

print("\t You will be asked for three strings")
print("\t which will be stored in a dictionary")
num_dict  = {}
prompt = "Enter a number :"
for i in range(3): # get three numbers
   x_str = input(prompt)
   num_dict[i] = x_str

print("\t Dictionary data structure: ",num_dict)
print("\t + First string: ",num_dict[0])
print("\t + First string: ",num_dict[1])
print("\t + First string: ",num_dict[2])
