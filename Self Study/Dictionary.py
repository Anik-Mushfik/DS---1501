### => Online class - Saddam sir - 15/11/2023

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
print(type(course[0]))

#update key value pairs
course[0]['title']='DS 151'
print(course)

#camp={'campus':'UIU', 'time':'1.51PM'}
course.append({'campus':'UIU', 'time':'1.51PM'})
print(course)
course.insert(1, {'trimester':'spring 2023', 'classmode':'hybrid'})
print(course)

del course[2]['instructor']
print(course)

#modifying a key
course[0]['course_name']=course[0].pop('title')
print(course)

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





### => 'Python Crash Course' Book -

# alien_0.py

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


# Try It Yourself - 6:
# 6-1. Person:
person = {
    'first_name': 'musfique', 
    'last_name': 'ahmed', 
    'age': 21, 
    'city': 'dhaka'
    }
full_name = person['first_name'].title() + " " + person['last_name']
print(f"A person I know -")
print(f"His name is {full_name}.\nHe is {person['age']} years old.")
print(f"He lives in {person['city']}.")

# 6-2. Favorite Number:
fav_num = {
    'musfique': 26, 
    'ahmed': 95, 
    'anik': 454, 
    'ripon': 36, 
    'akhi': 1385, 
    }
print(f"Musfique's favorite number is {fav_num['musfique']}")
print(f"Ahmed's favorite number is {fav_num['ahmed']}")
print(f"Anik's favorite number is {fav_num['anik']}")
print(f"Ripon's favorite number is {fav_num['ripon']}")
print(f"Akhi's favorite number is {fav_num['akhi']}")

# 6-3. Glossary:
glossary = {
    'print': 'Writes the output of the code in the terminal.', 
    'input': 'Takes command from the user.', 
    'terminal': 'The window in the compiler where the output is shown.', 
    'parentheses': 'First bracket', 
    'variable': 'Where a value of a code is stored.', 
    }
print(f"Print: {glossary['print']} \n")
print(f"Input: {glossary['input']}\n")
print(f"Terminal: {glossary['terminal']}\n")
print(f"Parentheses: \n     {glossary['parentheses']} \n")
print(f"Variable: \n    {glossary['variable']} \n")


# user.py
user_0 = {
    'username': 'efermi', 
    'first': 'enrico', 
    'last': 'fermi'
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


#favorite_language.py -
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phill': 'python',
    }
for name in favorite_language.keys():
    print(name.title())
for name in favorite_language: #Looping through keys of a dictionary is default.
    print(name)

friends = ['sarah', 'anik', 'phill']
for name in favorite_language:
    print(f"Hi {name.title()}")

    if name in friends: 
        language  = favorite_language[name].title()
        print(f"{name.title()}'s favorite language is {language}.")

if 'kallu' not in favorite_language.keys():
    print(f"Kallu please take our poll.")

for name in sorted(favorite_language.keys()):
    print(f"{name.title()}'s favorite language is {language}.")

for language in favorite_language.values():
    print(language.upper())

for language in set(favorite_language.values()):
    print(language.lower())


# TRY IT YOURSELF - 6
# 6-4. Glassary 2:
glossary = {
    'print': 'Writes the output of the code in the terminal.', 
    'input': 'Takes command from the user.', 
    'terminal': 'The window in the compiler where the output is shown.', 
    'parentheses': 'First bracket', 
    'variable': 'Where a value of a code is stored.', 
    }

glossary['title'] = 'Makes only the first carcter upper case and the rest lower case.'
glossary['upper'] = 'Makes all the caracters upper case.'
glossary['lower'] = 'Makes all the caracters lower case.'
glossary['rstrip'] = 'Deletes the space in the right last of the value.'
glossary['lsrtip'] = 'Deletes the space in the left last of the value.'

for word, meaning in glossary.items():
    print(f"\n{word.title()}:\t{meaning}")


# 6-5. Rivers:
rivers_of_countries = {
    'nile': 'egypt', 
    'padma': 'bangladesh', 
    'amazon': 'brazil', 
    'ganges': 'india',
    'mississippi': 'america', 
    'thames': 'england', 
    'murray': 'australia', 
    'orinoco': 'venezuela', 
    'saint lawrence': 'canada', 
    'danube': 'europe', 
    'mekong': 'vietnam', 
    }

for river, country in rivers_of_countries.items():
    print(f"The {river.title()} runs through {country.title()}.")
print()

for river in rivers_of_countries.keys():
    print(river.title())
print()

for country in rivers_of_countries.values():
    print(country.title())
print()


# 6-6. Pulling:
# favorite_language.py
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phill': 'python',
    'anik': 'r', 
    'mushfique': 'java'
    }

people = ['anas', 'anik', 'mahin', 'mushfique', 'abid', 'jenny', 'edward', 'jayid', 'jen', 'phil']

for person in people:
    if person in favorite_language.keys():
        print(f"Thank you {person.title()} for responding.")
    else:
        print(f"Hi {person.title()}! I have noticed that you didn't participated in the poll yet. Can you please respond fast?")


# aliens.py -
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien  = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print(f"Number of aliens: {len(aliens)}")


for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print()

for alien in aliens[:7]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:10]:
    print(alien)

    
# pizza.py -
pizza = {
    'crust': 'thick', 
    'toppings': ['mashrooms', 'extra cheez', 'pinaple']
    }

print(f"You ordered a {pizza['crust']} -crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping.title()}")

    
# favorite_language.py -
favorite_language = {
    'jen': ['python', 'rust'], 
    'sarah': 'c',
    'edward': ['rust'], 
    'phill': ['python', 'java', 'haskell'], 
    }

for name, languages in favorite_language.items():
    if len(languages) == 1:
        for language in languages:
            print(f"{name}'s favorite language is {language.title()}.")        
    else:
        print(f"{name}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")

            
# many_user.py -
users = {
    'musfique': {
        'first': 'musfique', 
        'last': 'ahmed', 
        'location': 'dhaka', 
        }, 
    
    'kallu': {
        'first': 'kallu',
        'last': 'mia', 
        'location': 'chor vata'
        }, 

    }

for user, info in users.items():
    print(f"Username: {user}")
    full_name = f"{info['first']} {info['last']}"
    print(f"\tFull name: {full_name.title()}")
    location = info['location']
    print(f"\tLocatio: {location.title()}")

    

# Try It Yourselt-6:
#6-7. People:
people = [
    {
        'first_name': 'musfique', 
        'last_name': 'ahmed', 
        'age': 21, 
        'city': 'dhaka'
    }, 
    {
        'first_name': 'kallu', 
        'last_name': 'mia', 
        'age': 121, 
        'city': 'chora'
    }, 
    {
        'first_name': 'hablu', 
        'last_name': 'dablu', 
        'age': 212, 
        'city': 'uganda'
    }, 
]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nName: {full_name.title()}"
          f"\nAge: {person['age']}"
          f"\nLocation: {person['city'].title()}")

          
#6-8. Pets:
pets = [
    {
        'animal_kind': 'cat', 
        'owner': 'nobita', 
    }, 
    {
        'animal_kind': 'dog', 
        'owner': 'tarif', 
    }, 
    {
        'animal_kind': 'anaconda', 
        'owner': 'anik', 
    }
]

for pet in pets:
    print(f"\nAnimal kind: {pet['animal_kind'].title()}"
          f"\nOwner name: {pet['owner'].title()}")

          
# 6-9. Favorite Places:
favorite_places = {
    'musfique': ['bd', 'us', 'uk', ], 
    'ahmed': ['aus', 'switzerland', ], 
    'anik': ['sajek']
}

for name, places in favorite_places.items():
    if len(places) == 1:
        for place in places:
            print(f"{name.title()}'s favorite place is {place.title()}")
    else:
        print(f"{name.title()}'s favorite places are:")
        for place in places:
            print(f"\t{place.title()}")

            
# 6-10. Favourite Numbers:
fav_num = {
    'musfique': [26, 83, 23, 3], 
    'ahmed': [95, 6, 374, 347, 85], 
    'anik': [454, 28, 37, 123], 
    'ripon': [36], 
    'akhi': [1385, 732354356], 
    }

for name, num in fav_num.items():
    print(f"{name.title()}'s favorite numbers are:")
    for n in num:
        print(n)

        
# 6-11. Cities:
cities = {
    'dhaka': {
        'country': 'bangladesh', 
        'population': 23209616, 
        'fact': 'it is the city of mousque', 
        }, 
    'chittagong': {
        'country': 'bangladesh', 
        'population': 5379660, 
        'fact': 'port city', 
        }, 
    'khula': {
        'country': 'bangladesh', 
        'population':  955104, 
        'fact': 'sundarban is located there',
    }, 
}

for city, info in cities.items():
    print(f"City name: {city.title()}")
    for key, value in info.items():
        # if type(value) == "<class 'int'>":
        #     print(f"\t{key.title()}: {value}")
        # else:
            # print(f"\t{key.title()}: {value.capitalize()}")
        print(f"\t{key.title()}: {value}")






### Random Problems:

## Write a Python program to sort (ascending and descending) a dictionary by value. :
#d = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(f"Original dictionary : {d}")

k = [x for x in d.keys()]
v = [y for y in d.values()]
s = {}
r = {}

for i in sorted(d.values()):
    key = k[v.index(i)]
    s[key] = d[key]
print(f"Dictionary in ascending order by value : {s}")

for i in sorted(d.values(), reverse=True):
    key = k[v.index(i)]
    r[key] = d[key]
print(f"Dictionary in descending order by value : {r}")


## Write a Python program to add a key to a dictionary. :
sample = {0: 10, 1: 20}
print(f"Sample Dictionary : {sample}")

sample[2] = 30 # Method-1
sample.update({3: 40}) # Method-2

print(f"Updated Result : {sample}")


## Write a Python script to concatenate the following dictionaries to create a new one. :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
new = {}

for i in (dic1, dic2, dic3):
    new.update(i)
print(new)

dic4 = {**dic1, **dic2, **dic3} # the ** unpacking operator to include the key-value pairs from multiple dictionaries.
print(dic4)


## Call an item from a nested dictionary :
import ipaddress


menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": {
                "cow milk": 15, 
                "goat milk": 20, 
            }, 
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

print(menu["latte"]["ingredients"]["coffee"])
for i, j in menu["latte"]["ingredients"]["milk"].items():
    print(f"{i} : {j}")


# w3 resource - 30:
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
things = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
no = [x for x in things.keys()]
amount = [y for y in things.values()]

for i in (sorted(amount, reverse=True)[:3]):
    ind = amount.index(i)
    print(f"{no[ind]} : {i}")


# Find out the unique values:
lst = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
value = []
for i in lst:
    value.append(*i.values())

snigle = []
double = []
for j in value: 
    if j not in snigle:
        snigle.append(j)
    else:
        double.append(j)

unique = []
for x in snigle:
    if x not in double:
        unique.append(x)
print(unique)


# Print all value once in a set:
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
u_value = set(val for dic in L for val in dic.values()) #set comprihension
print(u_value)
v_value = {val for dic in L for val in dic.values()}
print(v_value)

