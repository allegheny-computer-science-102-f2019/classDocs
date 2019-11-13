from pylab import plot, show, title, savefig, xlabel, ylabel, legend


s_str = "hello everyone" # define my string
s_dict = {} # define a dictionary to hold character information

# function to gather the counts of characters
for i in s_str: # go through the string, char by char
    if i not in s_dict:
        s_dict[i] = 1
    else:
        s_dict[i] = s_dict[i] + 1

print(" \t My string is: ",s_str)
print(" \t My encountered chars are :")
print(s_dict)

# determine the freqs

freq_list = [] # define a list to hold the freqs
for i in s_dict:
    freq_list.append(s_dict[i]/len(s_str))
print(freq_list)


# plot
x = [i for i in range(len(freq_list))]
y = freq_list

plot(x,y)
show()
