# Lesson 1: Python Basics - Variables, Data Types, Strings, Input
# Chalane ke liye: python python-basics/lesson01_basics.py

# ---------- 1. print (console.log jaisa) ----------
print("Assalam o Alaikum, Python!")
print("Ek", "se", "zyada", "cheezein")  # space ke saath print hoti hain

# ---------- 2. Variables (let/const nahi likhte) ----------
name = "Ali"
age = 25
height = 5.9
is_developer = True      # True/False capital se
nothing = None           # JS ka null

MAX_USERS = 100          # constant: sirf convention hai (CAPITAL naam)

# snake_case use hota hai, camelCase nahi
user_name = "ali_dev"

# ---------- 3. Data types ----------
print(type(name))          # <class 'str'>
print(type(age))           # <class 'int'>
print(type(height))        # <class 'float'>
print(type(is_developer))  # <class 'bool'>
print(type(nothing))       # <class 'NoneType'>

# ---------- 4. Type conversion ----------
print(int("10") + 5)       # 15
print(str(10) + "5")       # "105"
print(float("3.5"))        # 3.5
# print("10" + 5)          # ERROR! Python khud convert nahi karta (JS karta hai)

# ---------- 5. Math operators ----------
print(10 / 3)    # 3.333... (hamesha float)
print(10 // 3)   # 3  (floor division)
print(10 % 3)    # 1  (remainder)
print(2 ** 10)   # 1024 (power)

# ---------- 6. Strings ----------
first = "Ali"
last = 'Khan'
full = first + " " + last

# f-string = JS ka template literal `${}`
print(f"Mera naam {full} hai aur umar {age} saal")
print(f"Agle saal umar: {age + 1}")

msg = "  Hello FastAPI  "
print(msg.upper())         # toUpperCase()
print(msg.lower())
print(msg.strip())         # trim()
print(msg.replace("Hello", "Bye"))
print(len(msg))            # msg.length nahi, len(msg)
print("Fast" in msg)       # includes() -> True

# Slicing
word = "Python"
print(word[0])      # P
print(word[-1])     # n  (aakhri character)
print(word[0:3])    # Pyt
print(word[::-1])   # nohtyP (reverse)

# Multi-line string
bio = """Main full stack developer hoon.
Ab Python seekh raha hoon."""
print(bio)

# ---------- 7. Logical operators ----------
print(True and False)   # &&
print(True or False)    # ||
print(not True)         # !
print(5 == 5)           # Python mein === nahi hota, == hi strict hai

# ---------- 8. Input (user se lena) ----------
# input() hamesha string deta hai
# city = input("Aap ka shehar? ")
# print(f"{city} bohat acha shehar hai!")
