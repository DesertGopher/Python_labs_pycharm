print("Lab4 0022-04 - vegetables")
word1 = str(input("First vegetable: "))
word2 = str(input("Second vegetable: "))
word3 = str(input("Third vegetable: "))
Cword1 = str.capitalize(word1)
Cword2 = str.capitalize(word2)
Cword3 = str.capitalize(word3)
print(str.lower(word1),str.lower(word2),str.lower(word3))
print(str.upper(word1),str.upper(word2),str.upper(word3))
print ("Enter amount of ", str.capitalize(word1),":")
chars = set('0123456789$,')
n1 = (input())
while any((c not in chars) for c in n1):
    print ("You need to enter the number")
    n1 = (input())
print("Enter amount of ", str.capitalize(word2),":")
n2 = (input())
while any((c not in chars) for c in n2):
    print ("You need to enter the number")
    n2 = (input())
print ("Enter amount of ", str.capitalize(word3),":")
n3 = (input())
while any((c not in chars) for c in n3):
    print ("You need to enter the number")
    n3 = (input())
print("Format: {0}s: {1}, {2}s: {3}, {4}s: {5}.".format(Cword1, n1, Cword2, n2, Cword3, n3))
print("Print :",Cword1+"s:",n1+";",str.capitalize(word2)+"s:",n2+";",str.capitalize(word3)+"s:",n3+";")
