# =========================================
# PYTHON STRING METHODS (COMPLETE NOTES)
# Definition + Examples + Extra Practice
# =========================================


# =========================================
# 1. len()
# =========================================
# Definition:
# Returns total number of characters in a string (including spaces)

word = "Good Morning"
print(len(word))   # 12
print(len("Python Programming"))  # 18


# =========================================
# 2. capitalize()
# =========================================
#  Definition:
# Converts first letter to uppercase and rest to lowercase

s = "hello world"
print(s.capitalize())   # Hello world
print("python programming".capitalize())  # Python programming


# =========================================
# 3. split()
# =========================================
#  Definition:
# Splits string into list based on separator (default space)

text = "We are learning Python"
print(text.split())
# ['We', 'are', 'learning', 'Python']

data = "Apple,Banana,Mango"
print(data.split(","))

print("I love AI".split())  # extra example


# =========================================
# 4. replace()
# =========================================
#  Definition:
# Replaces old substring with new substring

msg = "I like cold coffee"
print(msg.replace("cold", "hot"))

sentence = "Python is easy"
print(sentence.replace("easy", "powerful"))

print("I love Java".replace("Java", "Python"))  # extra


# =========================================
# 5. find()
# =========================================
#  Definition:
# Returns index of first occurrence, else -1

s = "Hello World"
print(s.find("World"))   # 6
print(s.find("o"))       # 4
print(s.find("Java"))    # -1

print("Data Science".find("Science"))  # extra


# =========================================
# 6. index()
# =========================================
#  Definition:
# Same as find() but gives error if substring not found

s = "Programming"
print(s.index("g"))   # 3

print("Python".index("y"))  # extra example
# print("Python".index("z"))  # error


# =========================================
# 7. isalpha()
# =========================================
#  Definition:
# Returns True if string contains only letters

print("Hello".isalpha())
print("Hello123".isalpha())
print("Python".isalpha())

print("AI".isalpha())  # extra


# =========================================
# 8. isalnum()
# =========================================
#  Definition:
# Returns True if string contains only letters and numbers

print("Python3".isalnum())
print("Py 3".isalnum())
print("2026".isalnum())

print("AI2026".isalnum())  # extra


# =========================================
# 9. isdigit()
# =========================================
#  Definition:
# Returns True if string contains only digits

print("12345".isdigit())
print("12a45".isdigit())

print("2026".isdigit())  # extra


# =========================================
# 10. lower() / upper()
# =========================================
#  Definition:
# lower() → converts to lowercase
# upper() → converts to uppercase

s = "PyThOn"
print(s.lower())
print(s.upper())

name = "Vaibhav"
print(name.lower())
print(name.upper())

print("HELLO".lower())  # extra


# =========================================
# 11. title()
# =========================================
#  Definition:
# Capitalizes first letter of every word

text = "hello world python"
print(text.title())

print("data science ai".title())  # extra


# =========================================
# 12. count()
# =========================================
#  Definition:
# Counts number of occurrences of substring

t = "hello hello hello"
print(t.count("hello"))

s = "banana"
print(s.count("a"))

print("aaaa".count("a"))  # extra


# =========================================
# 13. strip()
# =========================================
#  Definition:
# Removes spaces from both left and right sides

s = "   hello   "
print(s.strip())

msg = "   Python   "
print(msg.strip())

print("   AI World   ".strip())  # extra


# =========================================
# 14. lstrip() / rstrip()
# =========================================
#  Definition:
# lstrip() → removes left spaces
# rstrip() → removes right spaces

s = "   hello   "
print(s.lstrip())
print(s.rstrip())

print("   data".lstrip())  # extra


# =========================================
# 15. islower() / isupper()
# =========================================
#  Definition:
# islower() → True if all letters are lowercase
# isupper() → True if all letters are uppercase

print("python".islower())
print("PYTHON".isupper())
print("PyThon".islower())

print("AI".isupper())  # extra


# =========================================
# 16. startswith() / endswith()
# =========================================
#  Definition:
# startswith() → checks starting word
# endswith() → checks ending word

s = "Hello World"
print(s.startswith("Hello"))
print(s.endswith("World"))

file = "image.png"
print(file.endswith(".png"))

print("data science".startswith("data"))  # extra


# =========================================
# 17. swapcase()
# =========================================
#  Definition:
# Converts uppercase ↔ lowercase

s = "PyThOn"
print(s.swapcase())

msg = "Hello World"
print(msg.swapcase())

print("Ai ML".swapcase())  # extra


# =========================================
# 18. join()
# =========================================
#  Definition:
# Joins elements of a list into a string

words = ["I", "love", "Python"]
print(" ".join(words))
print("-".join(words))

print(",".join(["A", "B", "C"]))  # extra


# =========================================
# 19. partition()
# =========================================
#  Definition:
# Splits string into 3 parts (before, separator, after)

s = "Hardworkpays"
print(s.partition("work"))

email = "test@gmail.com"
print(email.partition("@"))

print("Python-is-easy".partition("-"))  # extra


# =========================================
# 20. chaining methods
# =========================================
#  Definition:
# Using multiple string methods together

print("Hello World".upper().lower())
print("python programming".title().replace("Python", "Java"))

print("  ai world  ".strip().upper())  # extra


# =========================================
# 21. extra practice examples
# =========================================
a = "  hello python  "
print(a.strip().upper())

b = "data science"
print(b.title().count("A"))

c = "123Python123"
print(c.strip("123"))