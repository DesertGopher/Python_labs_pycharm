print("Lab5 0022-04 - quantities")
string = []
string2 = []
print("""
______________________________________________
Type in the list of line separated words.
Example: 
link 
site
force...
To leave the list press enter and type *q*
______________________________________________
""")
while (True):
    word = input("Your word: ")
    if (word[-1]) == 'q':
        break
    else:
        string.append(word)
string_set = set(string)
print("Your quantity: ", string_set)
space = len(str(string).split())
print("Your quantity contains", space, "words.")
lenth = str(string)
print("String lenth =", len(lenth) - (int(space) * 4))
print("Type in new list of", len(lenth) - (int(space) * 4), "symbols and same amount of words.")
for i in range(len(string)):
    word2 = input("Your word " + str(i + 1) + ": ")
    string2.append(word2)
d = {}
d = {string[i]: string2[i] for i in range(space)}
print("Your dictionary:")
print(d)
