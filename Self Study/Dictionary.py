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
