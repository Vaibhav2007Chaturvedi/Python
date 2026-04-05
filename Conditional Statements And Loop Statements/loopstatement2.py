# While Loop: we can execute a set of statements as long as a condition is true.
# EXAMPLE1:
# count=1
# while count<=5:
#     print(count)
#     count+=1

# EXAMPLE2:
# Python program to illustrate while loop with else statement
# x=0
# s=0
# while(x<10):
#     s=s+x
#     x=x+1
# else:
#     print("The sum of first nine integers : ",s)


# ...................................................
# INFINITE LOOPS:
# var=1
# while var==1:
#     num=int(input("Enter a Number"))
#     print("You Entered:",num)
# print("Good BYE!")

# ................................................

# NESTED LOOP: A loop may contain another loop as a part of its body.
# EXAMPLE1:

# i=2
# while(i>=0):
#     j=2
#     while(j>=0):
#         print(2,end=" ")
#         j=j-1
#     print()
#     i=i-1

# EXAMPLE2:
for i in range(1,4):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
    