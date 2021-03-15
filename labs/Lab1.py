print("Lab1 0022-04")

anumber = int(input("Enter your arbitrary number ") )
bnumber = int(input("Enter the border number "))
while anumber == bnumber :
     print ("Please, type different numbers. ")
     anumber = input("Enter your arbitrary number ")
     bnumber = input("Enter the border number ")
     if anumber != bnumber:
        break
n = 3*bnumber
if anumber < bnumber:
     print ("Your arbitrary number is less than border number.")
     print (anumber," < ",bnumber)
elif anumber > bnumber and anumber < n:
     print ("Your arbitrary number is more than border number.")
     print (anumber," > ",bnumber)
elif anumber >= n:
     print ("Your arbitrary number is more than border number in 3 times or more.")
     print (anumber," > ",n)
     print (n," = 3 *", bnumber)
