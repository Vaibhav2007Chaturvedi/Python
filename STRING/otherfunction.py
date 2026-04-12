# =========================================
#  OTHER STRING FUNCTIONS (ASCII / UNICODE)
# =========================================


# =========================================
#  Concept: ASCII / Unicode
# =========================================
# Characters in Python are internally stored as numbers.
# Each character has a unique number called ASCII / Unicode value.
# Example:
# A → 65
# a → 97


# =========================================
# 1. ord()
# =========================================
#  Definition:
# ord() returns ASCII / Unicode value of a character.

#  Examples
ch = 'b'
print(ord(ch))     # 98

print(ord('A'))    # 65
print(ord('a'))    # 97
print(ord('Z'))    # 90
print(ord('0'))    # 48


#  Extra Examples
print(ord('G'))    # 71
print(ord('m'))    # 109
print(ord('$'))    # 36
print(ord('@'))    # 64
print(ord(' '))    # 32 (space)


# =========================================
# 2. chr()
# =========================================
#  Definition:
# chr() returns character for a given ASCII / Unicode value.

#  Examples
print(chr(97))     # a
print(chr(66))     # B
print(chr(65))     # A
print(chr(122))    # z
print(chr(48))     # 0


#  Extra Examples
print(chr(100))    # d
print(chr(83))     # S
print(chr(36))     # $
print(chr(64))     # @
print(chr(32))     # space


# =========================================
#  IMPORTANT RELATIONSHIP
# =========================================
# ord() → character → number
# chr() → number → character

print(ord('A'))     # 65
print(chr(65))      # A


# =========================================
#  PRACTICAL USE CASES
# =========================================

# 1. Check ASCII range of letters
print(ord('A'), ord('Z'))   # 65 90
print(ord('a'), ord('z'))   # 97 122


# 2. Convert numbers to alphabets
for i in range(65, 70):
    print(chr(i), end=" ")
# Output: A B C D E


# 3. Convert alphabets to ASCII
for ch in "ABC":
    print(ord(ch))
# Output: 65 66 67