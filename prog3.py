# Write a temperature converter python program, which is menu driven. Each such
# conversion logic should be defined in separate functions. The program should call the
# respective function based on the user‘s requirement. The program should run as long as the
# user wishes so. Provide an option to view the conversions stored as list of tuples with attributes
# - from unit value, to unit value sorted by the user‘s choice (from-value or to-value).

history=[]
def ktoc(a):
    return a+273.15
def ctok(a):
    return a-273.15
def ctof(a):
    return  9.0/5.0 * a + 32
def ftoc(a):
    return (a - 32)  / 1.8 
def ftok(a):
    return 273.5 + ftoc(a)
def ktof(a):
    return 1.8*(ctok(a)) + 32

while(1):
    ch=int(input("1.Conversion\n2.History\n3.EXIT\nEnter your choice(int only):"))
    if ch==1:
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
        print("Ans:"+str(ans)+str(to))
        x=[val,unit,"to",ans,to]
        history.append(tuple(x))
    elif ch==2:
        print(history)
    elif ch==3:
        break
    else:
        print("Whats wrong with you!!!")