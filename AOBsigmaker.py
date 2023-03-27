def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1
aob1 = None
while True:
    sigChange = False
    if aob1 == None:
        aob1 = input("Enter first Array of Bytes: ")
    aob2 = input("Enter second Array of Bytes: ")
    if len(aob1) != len(aob2):
        raise ValueError(f"The lengths of the arrays do not match.\nLength AOB1: {len(aob1)}\nLength AOB2: {len(aob2)}\nAOB1: {aob1}\nAOB2: {aob2}")
    aob3 = []
    for i in range(len(aob1)):
        if aob1[i] == "?" or aob2[i] == "?":
            aob3.append("?")
            continue
        if aob1[i] != aob2[i]:
            aob3.append("?")
            print(f"Byte {i} changed to \"?\"")
            sigChange = True
            continue
        else:
            aob3.append(aob1[i])
    if sigChange == False:
        print("No improvements were made to the signature. Signature remains unchanged.")
    aob1 = listToString(aob3)
    print(aob1)
    aob2 = ""
    aob3 = []
