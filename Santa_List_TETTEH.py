# Daniel Tetteh
# 01.30.2026
# CMSC 150 - Section 02

import random

print("==Q2==")

nice_list = ["Nina", "Ravi", "Leila", "Amara", "Matteo", "Yara", "Jasper", "Linus", "Hiro", "Aiden", "D'Arcy", "Saoirse", "Ralphie", "Maya", "Isabella"]
naughty_list = ["Charlotte", "Kai", "Lukas", "Ethan"]
print(f"NICE list: {nice_list}")
print(f"NAUGHTY list: {naughty_list}")

print("==Q3==")

naughty_list.append("Dade")
print(f"NAUGHTY list: {naughty_list}")

print("==Q4==")

nice_list.remove("Linus")
naughty_list.insert(0,"Linus")
print(f"NICE list: {nice_list}")
print(f"NAUGHTY list: {naughty_list}")

print("==Q5==")

x = nice_list[:5]
y = naughty_list[3:6]
print("NICEST KIDS:")
for w in range(0,5):
    print(f"#{w+1} - {x[w]}")
print("NAUGHTIEST KIDS:")
for h in range(0,3):
    print(f"#{h+1} - {y[h-1]}")

print("==Q6==")

toy_list = ["iPhone 17 Pro", "Red Ryder BB Gun", "Scooter", "LEGOs", "Barbie Dreamhouse", "Tamagotchi", "Nintendo Switch 2", "Robux", "PLAY-DOH", "Squishmallow"] 
print(f"TOY list: {toy_list}")

print("==Q7==")

kids_list = []

for kid in nice_list:
    random.shuffle(toy_list)
    b = toy_list[:5]
    kids_list.append(b)
    print(f"{kid} - {b}")

print("==Q8==")

ralphie_index = 0

for i in range(len(nice_list)):
    if nice_list[i] == "Ralphie":
        ralphie_index = i
print(f"Ralphie's Toys: {kids_list[ralphie_index]}")

q = kids_list[ralphie_index]

for t in range(len(q)):
    if q[t] == "Red Ryder BB Gun":
        q[t] = "football"
print(f"Ralphie's New Toys: {q}")
