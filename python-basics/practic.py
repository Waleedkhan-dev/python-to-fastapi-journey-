age = 20 
if age >=18:
    print("Aap vote de sakte hain")

else:
     print("you are not eligible for vote ")


# ---------- 2. if / elif / else ----------

marks = 72 

if marks >= 80:
      grade = "A"
elif marks >= 70 :
        grade = "B"

elif marks >= 60:
        grade = "C"

else: 
    grade = "Fail"
print (f"marks: {marks}, Grade: {grade}")

# ---------- 3. and / or ke saath ----------

has_ticket = True
is_vip = False
if has_ticket and age>= 18:
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
      print(f"salm {name}")
else:
        print("Naam khaali hai")

# ---------- 7. while loop ----------

count = 1
while count <= 5:
      print(f"count {count}")
      count += 1
      print("while loop khatam")

# ---------- 7. while loop ----------

count = 1
while count <=5:
    print(f"count: {count}")
    count +=1
    print("print while loop khatm")
# ---------- 8. for loop + range ----------
for i in range(5):
      print(i, end= "")
      print()

for i in range(0,11,2):
      print(i, end= "")
      print()

for i in range(5,0,-1):
       print(i, end= "")
       print()
for letter in "python":
            print(letter, end= "-")
            print() 

total = 0
for n in range(1,11):
      total += n
print(f"Total: {total}")


for n in range(1,11):
     if n% 2 == 0:
           continue
     print(n, end= " ") 
     print()

for i in range (1,11):
    print(f"{num} x {i} = {num *i}")   # 55