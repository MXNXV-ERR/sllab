#AtomicDictnary.py
def AtomicDictionary() :
    element = {"Na": "Sodium", "Al": "Aluminium"}
    print(element)
    #Entering values into the dictionary
    unikey = input("Enter the symbol for a unique element pair\n")
    unisub = input("Enter the element name for {}\n".format(unikey))
    element.update({unikey: unisub})
    #Trying to enter duplicate values    
    unikey = input("Enter the symbol for a duplicate element\n ")
    unisub = input("Enter the element name for {}\n".format(unikey))
    element.update({unikey: unisub})
    print("The number of elements in the dictionary are {}".format(len(element)))
    #Search element in Dictionary
    se = input("Enter the element to search in the dictionary\n")
    if se in element.values():
        print("Element found")
    else:
        print("Element not found")
