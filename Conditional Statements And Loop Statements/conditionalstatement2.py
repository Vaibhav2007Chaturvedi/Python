#if-elif-else statement:
#        Each Condition is checked in order.If the  first is false,the next is checked and
#  so on.If one of them is true,the corresponding branch executes,and statement ends.

# EXAMPLE1:
# perc=float(input("Enter your percentage: "))
# if perc>=85:
#     print('A: ',perc)
# elif perc>=75 and perc<85:
#     print('B:',perc)
# elif perc>=55 and perc<75:
#     print('C:',perc)
# else:
#     print('F:',perc)
             
# Example2:
# salary=int(input("Enter Your Salary: "))
# if salary<=50000:
#     tax=0.05*salary
# elif salary<=60000:
#     tax=0.07*salary
# elif salary<=70000:
#     tax=0.08*salary
# else:
#     tax=0.10*salary
# print("Salary: " ,salary,"Tax :",tax)

# ................................................

# NESTED if-elif-else Statement: it allows you to check for multiple test expressions and 
#  executs different codes for more than two conditions.
# We can have an if-elif-else statement inside another if-else statement .
# This is called nesting in computer programming.

num=float(input("Enter a number: "))
if num>=0:
    if num==0:
        print("zero")
    else:
        print("positive number")
else:
    print("negative number")
    