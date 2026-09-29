# Lesson 2: Conditions (if/elif/else) aur Loops (while/for)
# Chalane ke liye: python python-basics/lesson02_conditions_loops.py

# ---------- 1. if / else ----------
age = 20
if age >= 18:
    print("Aap vote de sakte hain")
else:
    print("Abhi vote nahi de sakte")

# ---------- 2. if / elif / else ----------
marks = 72
if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"
print(f"Marks: {marks}, Grade: {grade}")

# ---------- 3. and / or ke saath ----------
has_ticket = True
is_vip = False
if has_ticket and age >= 18:
    print("Entry allowed")
if has_ticket or is_vip:
    print("Andar aa jayein")

# ---------- 4. Nested if ----------
is_logged_in = True
role = "admin"
if is_logged_in:
    if role == "admin":
        print("Admin dashboard")
    else:
        print("User dashboard")
else:
    print("Pehle login karein")

# ---------- 5. Truthy / Falsy ----------
name = ""
if name:
    print(f"Salam {name}")
else:
    print("Naam khaali hai")   # "" falsy hai

# ---------- 6. One-line if (ternary) ----------
status = "Adult" if age >= 18 else "Minor"
print(status)

# ---------- 7. while loop ----------
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
print("while loop khatam")

# ---------- 8. for loop + range ----------
for i in range(5):          # 0,1,2,3,4
    print(i, end=" ")
print()

for i in range(1, 6):       # 1 se 5
    print(i, end=" ")
print()

for i in range(0, 11, 2):   # 0,2,4,6,8,10
    print(i, end=" ")
print()

for i in range(5, 0, -1):   # 5,4,3,2,1
    print(i, end=" ")
print()

# ---------- 9. String par loop ----------
for letter in "Python":
    print(letter, end="-")
print()

# ---------- 10. Loop mein total ----------
total = 0
for n in range(1, 11):
    total += n
print(f"1 se 10 ka total: {total}")   # 55

# ---------- 11. break aur continue ----------
for n in range(1, 11):
    if n == 7:
        break               # loop yahin khatam
    if n % 2 == 0:
        continue            # even skip karo
    print(n, end=" ")       # 1 3 5
print()

# ---------- 12. Table (loop ka classic example) ----------
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
