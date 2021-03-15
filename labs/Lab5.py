print("Lab3(5) 0022-04")
string = []
string2 = []
print("""
______________________________________________
Type in the list of comma separated words.
Example: link, site, force...
To leave the list press enter and type |break|
______________________________________________
""")
while (True):
    word = input("Your words: ")
    if (word[-5]+word[-4]+word[-3]+word[-2]+word[-1]) == 'break':
         break
    else:
         string.append(word)
string_set = set(string)
print("Your quantity: ",string_set)
lenth = str(string)
print("String lenth =",len(lenth)-4)
print("Type in new list of ",len(lenth)-4,"symbols")
for i in range(len(string)):
    check = input()
    string2.append(check)
s = {string2[i]:string[i] for i in range(len(string))}
print(s)
