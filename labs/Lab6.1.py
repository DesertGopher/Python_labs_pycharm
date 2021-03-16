import random # для рандомных чисел
import math # для вычисления факториала и арккосинуса
print("""
Lab6.1 0022-04
Functions
""")
i = int(1)
chars = set('0123456789$,.-')
def add(p1, p2):
    return float(p1) + float(p2)
def sub(s1, s2):
    return s1 - s2
def mult(m1, m2):
    return m1 * m2
def div(d1, d2):
    return d1 / d2
def deg(deg1, deg2):
    return pow(deg1,deg2)
def module(mod):
    return abs(mod)
def rand(r1, r2):
    return random.uniform(r1, r2)
def fact(F):
    return math.factorial(F)
def acos(X):
    return math.acos(X)
while i < 2:
 print ("""
______________________________________________________
1.Sum   2.Subtraction   3.Multiplication   4.Division   
5.Degree   6.Module   7.Random   8.Factorial   9.Acos   
10.Exit\n
""")
 sign = input("Type in the number of operation: ")
 while (any((q not in chars) for q in sign)) or (float(sign) < 1 or float(sign) > 10):
     sign = input("There is no such operation. ")
 sign = str(sign)
 if sign == '1': #+
     p1 = input("Enter first number: ")
     while any((q not in chars) for q in p1):
        p1 = input("You should enter the number. ")
     p2 = input("Enter second number: ")
     while any((q not in chars) for q in p2):
        p2 = input("You should enter the number. ")
     p1 = float(p1)
     p2 = float(p2)
     print (p1, " + ",p2, " = ",add(p1, p2))
 elif sign == '2': #-
     s1 = input("Enter minued nimber: ")
     while any((q not in chars) for q in s1):
        s1 = input("You should enter the number. ")
     s2 = input("Enter subtrahend number: ")
     while any((q not in chars) for q in s2):
        s2 = input("You should enter the number. ")
     s1 = float(s1)
     s2 = float(s2)
     print (s1, " - ",s2, " = ", sub(s1, s2) )
 elif sign == '3': #*
     m1 = input("Enter first factor: ")
     while any((q not in chars) for q in m1):
        m1 = input("You should enter the number: ")
     m2 = input("Enter second factor: ")
     while any((q not in chars) for q in m2):
        m2 = input("You should enter the number: ")
     m1 = float(m1)
     m2 = float(m2)
     print (m1, " * ",m2, " = ", mult(m1, m2) )
 elif sign == '4': #/
     d1 = input("Enter the dividend: ")
     while any((q not in chars) for q in d1):
        d1 = input("You should enter the number: ")
     d2 = input("Enter divider: ")
     while any((q not in chars) for q in d2):
        d2 = input("You should enter the number: ")
     d1 = float(d1)
     d2 = float(d2)
     print (d1, "/",d2, " = ", div(d1, d2) )
 elif sign == '5': #degree
     deg1 = input("Enter the number: ")
     while any((q not in chars) for q in deg1):
        deg1 = input("You should enter the number: ")
     deg2 = input("Enter degree: ")
     while any((q not in chars) for q in deg2):
        deg2 = input("You should enter the number: ")
     deg1 = float(deg1)
     deg2 = float(deg2)
     print (deg1, "^",deg2, " = ", deg(deg1, deg2))
 elif sign == '6': #module
     mod = input("Enter your nubmer: ")
     while any((q not in chars) for q in mod):
        mod = input("You should enter the number: ")
     mod = float(mod)
     print ("|",mod,"| "" = ", module(mod))
 elif sign == '7': #random
     print ("Enter the right and left boundaries of the range: ")
     r1 = input("Left: ")
     while any((q not in chars) for q in r1):
        r1 = input("You should enter the number: ")
     r2 = input("Right: ")
     while (any((q not in chars) for q in r2)) or (float(r2) < float(r1)):
         while any((q not in chars) for q in r2):
             r2 = input("You should enter the number: ")
         while float(r2) < float(r1):
            print ("Right border must be more than left one.")
            r2 = input("Right:")
     r1 = float(r1)
     r2 = float(r2)
     print ("Random [",r1,";",r2,"] = ",rand(r1, r2))
 elif sign == '8': #factorial
     F = input("Enter the integer: ")
     while any((q not in chars) for q in F) or float(F) % 1 > 0:
        if any((q not in chars) for q in F):
           F = input("You should enter the number: ")
        elif float(F) % 1 > 0:
          F = input("You need to enter the integer: ")
     F = int(F)
     print(F, "! = ", fact(F))
 elif sign == '9': # acos
     X = input("Enter the number (-1;1): ")
     while any((q not in chars) for q in X) or (float(X) > 1 or float(X) < -1):
          if any((q not in chars) for q in X):
             X = input("You should enter the number: ")
          elif float(X) > 1 or float(X) < -1:
             print ("You number must be between 0 and 1 to find acos.")
             X = input("Enter the number (-1;1): ")
     X = float(X)
     print("acos(",X,") = ",acos(X), "rad")
     print("acos(",X,") = ", acos(X)*180/math.pi,"°")
 elif sign == '10':
      exit()