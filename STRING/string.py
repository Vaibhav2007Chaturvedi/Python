# String: String are collection of characters in contiguous memory location.
#   surrounded by single(' ') or double(" ") quotes is known as a string

# Creating String:
str1="Hello World"
print(str1)

# ..............................................
# Using Quotes inside a string:
# CASE1:String has single quote
#   use:Double quotes or escape with \

# a="This is Meera's pen"
a='This is Meera\'s pen'
print(a)

# CASE2: String has double quote
#  Use single quotes:
b='Write an article on "AI" briefly .'
print(b)

# CASE3: String has both single and double quotes
#   USE: escape\
c="She said,\"I'll call you.\""
print(c)

# .....................................................

# ESCAPE CHARACTER(\):Used to handle special character ,called escape sequence.
# Common Example:  1) \' -> single quote  , 2) \" -> double quotes , 3)\n ->New line

# ............................................................

# Empty String: An empty string is a string with no characters and its length=0.
#   EXAMPLE:
s=" "
print(s)

#.............................................................

# Line Continuation(\):Used to break a long line into multiple line.
#   But output will still come in one line.
# Example:
a="We are Indians and" \
 "We love our country"
print(a)

# ...............................................................

#Escape sequence(\n): Used to print text in next line.
# Example:
c="We are Indians\nand we love our country"
print(c)

# ...................................................................

# Space Using Escape(\t): \t gives Horizontal space(tab space).
# Example:
print("Hello\tWorld")

# .....................................................................

# Multiline Strings : used to  write text in multiple lines easily.
#   use:1)  ''' '''(triple single quotes)
#        2) """ """(triple double quotes)

a="""This is a multiline string
we are stydents
We study Python"""
print(a)
#.........................................................................#
