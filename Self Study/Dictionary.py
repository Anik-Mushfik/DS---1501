### => Online class - Saddam sir - 15/11/2023
"""
#Printing from a dictionary -
human = {'name': 'rubayet', 'gender': 'male', 'age': 25}
print(human['age'])

#Adding to a dictionary - 
human = {}
human['dept'] = 'CSE'
human['profession'] = 'student'
print(human)

#Deleting an item - 
del human['dept']
print(human)

#Using for loop in a dictionary - 
favorite_lan = {'miti': 'python', 'raufur': 'c', 'anas': 'rubi', 'inan': 'python', 'sakib': 'java'}
print(f"Favorite language of Miti is {favorite_lan['miti'].title()}")
for key, value in favorite_lan.items():
    print("Key: " + key + " , " + " Value: " + value)

#Printing only keys or values - 
for key in favorite_lan.keys():
    print("Key: " + key)
for value in favorite_lan.values():
    print("Value: " + value)

#Sorting dictionary - 
for k in sorted(favorite_lan.keys()):
    print("Key: " + k)
for v in sorted(favorite_lan.values()):
    print("Value: " + v)

#Not reapiting a value multiple times:
for v in set(favorite_lan.values()):
    print("Value: " + v)

#Multiple dictionaries in a list -
course = [
{
    'title': 'DS 1501', 
    'credit': 3
}, 
{
    'instructor': 'Dr. Ahmed', 
    'duration': 1
}, 
{
    'book':  'python crash course', 
    'pages': 90
}
]
print(course)
print(len(course))
print(course[0])
print(course[0].values())
print(course[0]['title'])

#Adding to a list of dictionary - 
course.append({'campus': 'united city', 'class mode': 'hybrid'})
course.insert(2, {'trimester': 'fall-2023', 'season': 'sep-jan'})
print(len(course))
print(course)

#List in a dectionary -
tracks = {
    "software": ['project management', 'system analysis', 'soft engg'], 
    "iot": ['cloud computing', 'green computing', 'robotics'],
    "hardware": ['computer architecture', 'DLD', 'microprocessor'], 
    "machine learning": ['pattern rec', 'immage tracking']
}
print(tracks["iot"])
print(tracks["iot"][0])
for i in tracks["iot"]:
    print(i)
for k, v in tracks.items():
    print(k, v)
    for i in v:
        print(f"{k}: {i}")
    print()
"""




### => 'Python Crash Course' Book -

# alien_0.py
"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

print(f"Congratulations! You have earned {alien_0['points']} points.")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")

alien_0 = {'color': 'green', 'points': 5, 'x_position': 10, 'y_position': 25, 'speed': 'fast'}
speed = input("Enter the speed of the alien: (Slow / Medium / Fast)\n").lower()
alien_0['speed'] = speed

# Move the alien to the right and up.
# Determine how far to move the alien based on the current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
    y_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
    y_increment = 2
else:
    #This is a fast alien!
    x_increment = 3
    y_increment = 3

# New position is the current position plus the increments.
alien_0['x_position'] = alien_0['x_position'] + x_increment
alien_0['y_position'] = alien_0['y_position'] + y_increment

print(f"The new position of the alien is - \n X position: {alien_0['x_position']} \n Y posiotion: {alien_0['y_position']}")

alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)

#favorite_language.py -
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phill': 'python',
    }
print(favorite_language)
favorite_language['noah'] = 'java'
print(favorite_language)

language = favorite_language['noah'].title()
print(f"Noah's favorite language is {language}.")

# alien_0.py
alien_0 = {'color': 'green', 'points': 5}
speed_value = alien_0.get('speed', "This key doesn't exist.")
speed_value2 = alien_0.get('speed')
print(speed_value)
print(speed_value2) # This will print 'None' and 'None' means - 'no value exist'
"""
