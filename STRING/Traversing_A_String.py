# Traversing A String:
#        It means accessing each character one after the other by iterating through
#         the elements of a string using either for or while loops.

#1)) Iterating Through string using for loop 
                                            
# str='Computer Science'
# for i in str:
#     print(i)
# -------------------------------------------------
#2)) Iterating through string using while loop

# str1='Python Programming'
# index=0
# while index<len(str1):
#     print(str1[index],end="\n")
#     index =index+1

# .........................................................

# Write A program to count the number of times a character occurs in a string:
# str=input("Enter a string: ")
# ch=input("Enter a character to be search :")
# count=0
# for character in str:
#     if character==ch:
#         count+=1
# print("The number of character",ch,"occurs in a string",count)

# ----------------------------------------------------

# Write a program to display string in reverse order:
str=input("Enter a String : ")
for i in range(-1,-len(str)-1,-1):
    print(str[i],end=" ")