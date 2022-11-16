# Python Classes: Write a python class to reverse a sentence (initialized via constructor) word
# by word. Example: “I am here” should be reversed as “here am I”. Create instances of this
# class for each of the three strings input by the user and display the reversed string for each, in
# descending order of number of vowels in the string.

#define class Reverse
class Reverse:
    string=""
    def __init__(self,string):
        self.string=" ".join(reversed(string.split()))
       

print("Enter 3 strings")
objArr=[]
countVowels = [0, 0, 0]
dict = {}
for i in range(3):
    objArr.append(Reverse(input()))
    for j in range(len(objArr[i].string)):
        #Counting the vowels
        if objArr[i].string[j].lower() in ['a', 'e', 'i', 'o', 'u']:
             countVowels[i] += 1
    #Add to  Dictionary 
    dict.update({objArr[i].string:countVowels[i]})
print("Sorted in descending order of vowels in each")
#Print in sorted order of number of vowels from dictionary
print(*sorted(dict.items(),key=lambda x:x[1],reverse=True),sep="\n")
