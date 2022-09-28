# Write Python code to do the following:
# i. Create list with inputs from user
# ii. Determine minimum and maximum elements in the list
# iii. Insert new element into the list
# iv. Delete an element from the list
# v. Determine if an element is present in the list

li=[]
n= input("Enter number of elements")
print("Enter "+ n + " values")
for i in range(int(n)):
    li.append(int(input()))
while 1:
    c=int(input("1.Insert\n2.Delete\n3.Find ele\n4.MINMAX\n5.Print\n6.EXIT\nEnter your choice"))
    if c==1:
        li.insert(int(input("Enter pos")),int(input("Enter ele")))
        print(li)
    elif c==2:
        try:
            li.remove(int(input("Enter ele to del")))
            print(li)
        except:
            print("Ele doesn't exists")
    elif c==3:
        try:
            pos=li.index(int(input("Find ele")))
            print("Element found at" + str(pos))
        except:
            print("Element not found")
        print(li)
    elif c==4:
        print("MAX:"+str(max(li))+"\nMIN:"+str(min(li)))
        print(li)
    elif c==5:
        print(li)
    else:
        break