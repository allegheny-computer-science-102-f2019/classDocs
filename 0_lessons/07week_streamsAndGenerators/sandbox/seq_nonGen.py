# Build and return a list
# ref: https://wiki.python.org/moin/Generators
def listBuilder(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums
#end of listBuilder()
sum_of_first_n = sum(listBuilder(1000000))
print("sum of first n :",sum_of_first_n)
