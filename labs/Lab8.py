import random  # для рандомных чисел
import math  # для вычисления факториала и арккосинуса

print("Lab8 0022-04 - Classes")
i = int(1)
chars = set('0123456789$,.-')


class Operation:
    tip = "Sum"

    def display_info(self):
        print("\033[32mOperation\033[30m :", self.tip)


operation1 = Operation()  # +
operation2 = Operation()  # -
operation2.tip = "Subtraction"
operation3 = Operation()  # *
operation3.tip = "Multiplication"
operation4 = Operation()  # /
operation4.tip = "Division"
operation5 = Operation()  # degree
operation5.tip = "Degree"
operation6 = Operation()  # module
operation6.tip = "Module"
operation7 = Operation()  # rand
operation7.tip = "Random"
operation8 = Operation()  # factorial
operation8.tip = "Factorial"
operation9 = Operation()  # acos
operation9.tip = "Acos"
while i < 2:
    print("""
______________________________________________________
1.Sum   2.Subtraction   3.Multiplication   4.Division   
5.Degree   6.Module   7.Random   8.Factorial   9.Acos   
10.Exit\n
""")
    sign = input("Type in the number of operation: ")
    while (any((q not in chars) for q in sign)) or (float(sign) < 1 or float(sign) > 10):
        sign = input("There is no such operation. ")
    sign = str(sign)
    if sign == '1':  # +
        operation1.display_info()
        p1 = input("Enter first number: ")
        while any((q not in chars) for q in p1):
            p1 = input("You should enter the number. ")
        p2 = input("Enter second number: ")
        while any((q not in chars) for q in p2):
            p2 = input("You should enter the number. ")
        p1 = float(p1)
        p2 = float(p2)
        print(p1, " + ", p2, " = ", p1 + p2)
    elif sign == '2':  # -
        operation2.display_info()
        s1 = input("Enter minued nimber: ")
        while any((q not in chars) for q in s1):
            s1 = input("You should enter the number. ")
        s2 = input("Enter subtrahend number: ")
        while any((q not in chars) for q in s2):
            s2 = input("You should enter the number. ")
        s1 = float(s1)
        s2 = float(s2)
        print(s1, " - ", s2, " = ", s1 - s2)
    elif sign == '3':  # *
        operation3.display_info()
        m1 = input("Enter first factor: ")
        while any((q not in chars) for q in m1):
            m1 = input("You should enter the number: ")
        m2 = input("Enter second factor: ")
        while any((q not in chars) for q in m2):
            m2 = input("You should enter the number: ")
        m1 = float(m1)
        m2 = float(m2)
        print(m1, " * ", m2, " = ", m1 * m2)
    elif sign == '4':  # /
        operation4.display_info()
        d1 = input("Enter the dividend: ")
        while any((q not in chars) for q in d1):
            d1 = input("You should enter the number: ")
        d2 = input("Enter divider: ")
        while any((q not in chars) for q in d2):
            d2 = input("You should enter the number: ")
        d1 = float(d1)
        d2 = float(d2)
        print(d1, "/", d2, " = ", d1 / d2)
    elif sign == '5':  # degree
        operation5.display_info()
        deg1 = input("Enter the number: ")
        while any((q not in chars) for q in deg1):
            deg1 = input("You should enter the number: ")
        deg2 = input("Enter degree: ")
        while any((q not in chars) for q in deg2):
            deg2 = input("You should enter the number: ")
        deg1 = float(deg1)
        deg2 = float(deg2)
        print(deg1, "^", deg2, " = ", pow(deg1, deg2))
    elif sign == '6':  # module
        operation6.display_info()
        mod = input("Enter your nubmer: ")
        while any((q not in chars) for q in mod):
            mod = input("You should enter the number: ")
        mod = float(mod)
        print("|", mod, "| "" = ", abs(mod))
    elif sign == '7':  # random
        operation7.display_info()
        print("Enter the right and left boundaries of the range: ")
        r1 = input("Left: ")
        while any((q not in chars) for q in r1):
            r1 = input("You should enter the number: ")
        r2 = input("Right: ")
        while (any((q not in chars) for q in r2)) or (float(r2) < float(r1)):
            while any((q not in chars) for q in r2):
                r2 = input("You should enter the number: ")
            while float(r2) < float(r1):
                print("Right border must be more than left one.")
                r2 = input("Right:")
        r1 = float(r1)
        r2 = float(r2)
        print("Random [", r1, ";", r2, "] = ", random.uniform(r1, r2))
    elif sign == '8':  # factorial
        operation8.display_info()
        F = input("Enter the integer: ")
        while any((q not in chars) for q in F) or float(F) % 1 > 0:
            if any((q not in chars) for q in F):
                F = input("You should enter the number: ")
            elif float(F) % 1 > 0:
                F = input("You need to enter the integer: ")
        F = int(F)
        print(F, "! = ", math.factorial(F))
    elif sign == '9':  # acos
        operation9.display_info()
        X = input("Enter the number (-1;1): ")
        while any((q not in chars) for q in X) or (float(X) > 1 or float(X) < -1):
            if any((q not in chars) for q in X):
                X = input("You should enter the number: ")
            elif float(X) > 1 or float(X) < -1:
                print("You number must be between 0 and 1 to find acos.")
                X = input("Enter the number (-1;1): ")
        X = float(X)
        print("acos(", X, ") = ", math.acos(X), "rad")
        print("acos(", X, ") = ", math.acos(X) * 180 / math.pi, "°")
    elif sign == '10':
        exit()
