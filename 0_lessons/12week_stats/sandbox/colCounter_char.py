''' Print the number of times a Character has occurred in list'''

from collections import Counter
scores_list = ['a','b','a','a','b','c']
x_colCount = Counter(scores_list)
print("type(x_colCount)",type(x_colCount))" # <class 'collections.Counter'>
print("  Data: ",scores_list)
print(" + One way to collect counts:\n")
print("  Value\tCount")
for i in x_colCount:
	print("  ",i,"\t",x_colCount[i])
print("\n + Another way to collect counts:\n")
for i in x_colCount.most_common():
	print("  ",i)
