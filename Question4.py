# Write a temperature converter python program, which is menu driven. Each such
# conversion logic should be defined in separate functions. The program should call the
# respective function based on the user‘s requirement. The program should run as long as the
# user wishes so. Provide an option to view the conversions stored as list of tuples with attributes
# - from unit value, to unit value sorted by the user‘s choice (from-value or to-value).

#inital list to store conversion
history=[]
#converion logic for temprature
def ktoc(a):
    return a-273.15
def ctok(a):
    return a+273.15
def ctof(a):
    return  9.0/5.0 * a + 32
def ftoc(a):
    return (a - 32)  / 1.8 
def ftok(a):
    return 273.5 + ftoc(a)
def ktof(a):
    return 1.8*(ctok(a)) + 32
#infinite loop for menu driven approach
while(1):
    print("Main Menu".center(40,"#"))
    ch=int(input("1.Conversion\n2.History\n3.EXIT\nEnter your choice(int only):"))
    if ch==1:#conversion based on user choice
        n=input("Enter temperature you would like to convert with unit(Eg:20C,50.00k...):")
        val=float(n[:-1])
        unit=n[-1].upper()
        to=input("Enter the unit to which u wanna convert(c/f/k)").upper()
        if unit=="K" and to=="C":
            ans=ktoc(val)
        elif unit=="K" and to=="F":
            ans=ktof(val)
        elif unit=="C" and to=="F":
            ans=ctof(val)
        elif unit=="C" and to=="K":
            ans=ctok(val)
        elif unit=="F" and to=="C":
            ans=ftoc(val)
        elif unit=="F" and to=="K":
            ans=ftok(val)
        elif unit==to:
            print("Something is really wrong with you!!!!")
            continue
        else:
            print("Invalid input!!!")
            continue
        #save the conversion in tuple and append to list
        print("Ans:"+str(ans)+str(to))
        x=[val,unit,"to",round(ans,3),to]
        history.append(tuple(x))
    elif ch==2:#print all the executed conversions
        c=input("1.Order by from-value\n2.Order by to-value\nEnter your choice:")
        print("😏=H=I=S=T=O=R=Y".center(40,"="))
        if c=='1':#ordered by from-value
            print(*sorted(history,key=lambda x:x[0]),sep="\n")
        elif c=='2':#ordered by to-value
            print(*sorted(history,key=lambda x:x[3]),sep="\n")
        else:
            print("Invalid input,kid!!!")
    elif ch==3:
        break
    else:
        print("Whats wrong with you!!!")