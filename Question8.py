# Python: Create a list of 6 numbers. Use ‘list-comprehension’ to create a new list where each
# element in the original list is multiplied by 3. Use ‘lambda’ and ‘reduce’ function find the
# sum of the elements of the original list as well as the new list.

from functools import reduce

urlist=[]
print("Enter 6 Numbers:\n")
for i in range(6):
    urlist.append(int(input()));
print(urlist)
ur2list=[(lambda x: 3*x) (x) for x in urlist]
print(ur2list)
print(reduce(lambda a,b:a+b,urlist))