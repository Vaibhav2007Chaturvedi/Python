# SPECIAL STRING OPERATIONS:
# 1) Concatenating String: means to create a new string by adding two strinng.
s1="Hello"
s2="world"
print(s1+s2) #Helloworld
# NOTE:You Cannot add 'str' and 'int' objects.
# print(2+'book') #ERROR 
# Example2:
print('6'+'3') #63
print(6+3) #9
# .....................................

# 2)Replicating String: The * operator create a new string by repeating multiple copies of the same string.
print(3*'hello') #hellohellohello
print(2*'2') #22
# NOTE: The * Operator has to either have both operands of the number types (for performing multiplication) or one string type and one number type(for repition). It cannot work with both operands of strings type. 
# print('3'*'4') #Error:
# The last statement shall result in an error because string cannot be multiplied.

# .........................................

# 3)Membership Operators:Python offers two membership operators for checking whether a particular character exists in the given string or not. These operators are 'in' and 'not in'.
# 'in' operator: It return true if a character/substrinng exists in the given string.
# 'not in' operator: It returns true if a character/substring does not exist in the give string.
# Example:
print('H' in 'Hello') #TRUE
print('y' in "hello") #FALSE
print('y' is not 'hello') #TRUE
print('h' is not 'hello') #TRUE
# NOTE: To use membership operator inn string ,it required that both the operands used should be of strinng type.

# ..........................................

# 4)Comparison Operators: Use relational/comparison operators(>,<,>=,<=,==,!=) to compare two string.
str1="mary"
str2="mac"
print(str1<str2) #FALSE
print(str1!=str2) #TRUE
print(str1>=str2) #TRUE

# NOTE: Python compares two strings character by character according to their Unicode values , until it finds element that differ.Subsequent elements are not considered.

# ........................................

# 5)String Slicinng: String Slicing in Python is used to extract a part (substring) of a strinng using index position. 
# NOTE: FORMAT: string[start:end:stop]
# EXAMPLE:
A='SAVE MONEY'
print(A[1:3]) #AV
print(A[:3]) #SAV
print(A[3:]) #E MONEY
print(A[:]) #SAVE MONEY
print(A[-2:]) #EY
print(A[:-2]) #SAVE MON
print(A[::2]) #SV OE
 
# .........................................

#Write a program to input name and print the pattern using string slicing:
name=input("Enter a name: ")
for i in range(0,len(name)+1):
    print(name[0:i])
# Enter a name: Vaibhav

# V
# Va
# Vai
# Vaib
# Vaibh
# Vaibha
# Vaibhav

# ......................................

# String Are Immutable: In python,string are immutable which means: Once a string is created , it cannot be changed(modified).
s="Hello"
# s[0]="Y"
# print(s[0]) #Error 

# Correct way:
s="Y"+s[1:]
print(s) #Yello