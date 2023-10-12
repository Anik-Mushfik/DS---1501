# Solution of problem - 2.1(A):
names = ["Musfique", "Ahmed", "Anik"]
print(names[0])
print(names[1])
print(names[2])

# Solution of problem - 2.1(B):
print("Good morning, " + names[0] + ".")
print("Good morning, " + names[1] + ".")
print("Good morning, " + names[2] + ".")

# Solution of problem - 2.1(c):
favorite_cars = ["Bugatti", "Ferrari", "Lamborgini"]
print("I would like to own a " + favorite_cars[1] + " car.")
print("I would love to own a " + favorite_cars[2] + " car.")
print("I would like to own a " + favorite_cars[0] + " car.")

#Solution of problem - 2.2(A):
invited_people = ["Musfique", "Ahmed", "Anik"]
print("Hi! " + invited_people[0] + ". I would like to invite you to dinner tomorrow.")
print(f"Hi! {invited_people[1]}. I would like to invite you to dinner tomorrow.")
print(f"Hi! {invited_people[2]}. I would like to invite you to dinner tomorrow.")

#Solution of problem - 2.2(B):
print(f"Ahmed won't be able to attend the dinner tonight.")
invited_people[1] = "Akhi"
print(f"Hey, {invited_people[0]}! How are you doing? I just wanted to remind you about the dinner tonight.")
print(f"Hi! {invited_people[1]}. I would like to invite you to dinner tonight.")
print(f"Hey, {invited_people[2]}! I just wanted to remind you about the dinner tonight. See you later.")

#Solution of problem - 2.2(C):
print("Exciting news! I just found a bigger table.")
invited_people.insert(0, "Ripon")
invited_people.insert(2, "Sami")
invited_people.append("Tarif")
message = "You are invited to a fun dinner to my house tonight."
print(invited_people)
print(f"Hey! {invited_people[0]} {message}.")
print(f"Hey! {invited_people[1]} {message}")
print(f"Hey! {invited_people[2]} {message}")

for people in invited_people:
    print(f"Hey! {people}, {message}")



#Solution of problem - 2.2(D):
