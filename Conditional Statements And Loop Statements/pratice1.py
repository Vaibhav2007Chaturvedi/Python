# Write a program for leap year:
# year=int(input("Enter 4 digit year: "))
# if (year%400==0) or(year%4==0 and year%100!=0):
#     print("Leap Year")
# else:
#     print("Not A Leap Year")

# ..............................................

# Write A Program to find the largest nummber among three inputted number:
# a=int(input("Enter First Number: "))
# b=int(input("Enter Second Number: "))
# c=int(input("Enter Third Number: "))
# if (a>b and a>c):
#     print("A is the greatest number: ",a)
# elif(a<b and b>c):
#     print("b is the greatest number: ",b)
# elif(c>a and c>b):
#     print("c is the greatest numbber: ",c)
# else:
#     print("Give input")

# ...................................................

# Write A Program to display sum of even numbers up to number n entered by the user:
# s=0
# n=int(input("Enter A Number: "))
# for i in range(n+1):
#     if i%2==0:
#         s+=i
# print(s)

# .............................................

# Write A Program that Reads two number and an arithmetic operators and display the result:
# a=int(input("Enter A First Number: "))
# b=int(input("Enter A Second Number: "))
# op=input("Enter the operator: ")
# if op=='+':
#     print("A+B= ",a+b)
# elif op=='-':
#     print("A-B= ",a-b)
# elif op=='*':
#     print("A*B= ",a*b)
# elif op=='/':
#     print("A/B= ",a/b)
# elif op=='**':
#     print("A**B= ",a**b)
# else:
#     print("INVALID")

# ...............................................

# Write A program according to user choice using menu:
# a)Area of circle , b)Area of rectangle ,c)Circumference of circle and d)Area of Square
while True:
    print("\nMENU")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Circumference of Circle")
    print("4. Area of Square")
    print("0. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        r = float(input("Enter the radius of circle: "))
        area = 3.14 * r * r
        print("Area of Circle:", area)

    elif ch == 2:
        l = float(input("Enter length of rectangle: "))
        b = float(input("Enter width of rectangle: "))
        area = l * b
        print("Area of Rectangle:", area)

    elif ch == 3:
        r = float(input("Enter the radius of circle: "))
        circumference = 2 * 3.14 * r
        print("Circumference of Circle:", circumference)

    elif ch == 4:
        s = float(input("Enter side of square: "))
        area = s * s
        print("Area of Square:", area)

    elif ch == 0:
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please try again.")