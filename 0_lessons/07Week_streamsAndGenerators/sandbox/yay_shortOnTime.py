# short on time? 
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        print(my_str[i])
        yield my_str[i]



seq = "This is a short sequence"
a = rev_str(seq)

for i in range(len(seq)):
    next(a)


