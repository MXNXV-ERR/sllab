# Python File Handling & List Comprehension: Write a python program to read the contents of a
# file (filename as argument) and store the number of occurrences of each word in a dictionary.
# Display the top 10 words with most number of occurrences in descending order. Store the length of
# each of these words in a list and display the list. Write a one-line reduce function to get the average
# length and one-line list comprehension to display squares of all odd numbers and display both.

from functools import reduce
from collections import Counter
f=open("counting.txt")
#make a text file say counting.txt(in same folder)
contents=f.read().split()
print("\nFile Contents:")
print(*contents,sep=' ')
count_dict = Counter(contents)
print("\n\n",count_dict)
print("\n10 Words in decreasing order of occurance:")
s=(sorted(count_dict.items(),key=lambda x:x[1],reverse=True))
print(s[:10])
wordlen=[len(i) for i,j in s[:10]]
print("\nList with length of each word:\n",wordlen)
avg=(reduce(lambda x,y:x+y,wordlen))/len(wordlen)
print("Avg: ",avg)
sq_odd=[i*i for i in wordlen if i%2!=0]
print("Square of odd numbers: \n",sq_odd)