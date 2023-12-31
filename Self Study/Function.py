## Ex - 1:
# greeter.py
def greet_user():
    """Display a simple greeting."""
    print("Hello World!")

greet_user()
# greeter.py
def greet_user(username):
    """Display a simple greeting with a name."""
    print(f"Hello, {username}!")

greet_user("Musfique")


## T I Y -
# 8-1:
def display_message(x):
    """Describes what I am learning about in this chapter."""
    print(f"I am learning about {x} in this chapter.")

display_message("Functions")

# 8-2:
def favourite_book(X):
    print(f"My favorite book is {X}")

favourite_book("Alice in Wonderland")


## Ex - 2:
# pets.py
def describe_pet(animal_type, pet_name):
    """Describe information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet("cat", "hogi") # Order matters
describe_pet("hamster", 'sala')
describe_pet(animal_type='dog', pet_name='kutta') # Order doesn't matter for keyword arguments.
describe_pet(pet_name='sagol', animal_type="cow")

def describe_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s nami is {pet_name}")

describe_pet('kutta')
describe_pet(pet_name='kutta')
describe_pet('sagol', 'cow')
describe_pet('cow', 'sagol') # Ye galat haye
describe_pet(animal_type='cow', pet_name='sagol') # Ye sahi haye


## T I Y -
# 8-3. T-shirt:
def make_shirt(size, message):
    """Print a sentence summarizing- 
    The size of the shirt and The message printed on it."""
    print(f"\nHere is the summary of the T-shirt:")
    print(f'''\tSize: {size} 
        Message: {message}''')
    
make_shirt('XL', "Data Science Department Tour - 2024")
make_shirt(message='Data Science Department Tour - 2024', size="XXL")

# 8-4. Large Shirt:
def make_shirt(size='L', message="I love Python!"):
    """Print a sentence summarizing- 
    The size of the shirt and The message printed on it."""
    print(f"\nHere is the summary of the T-shirt:")
    print(f'''\tSize: {size} 
        Message: {message}''')
    
make_shirt()
make_shirt(size='M')
make_shirt(size="Any Size", message="All my friends are TOXIC!\n\t\t They are so rude and always negative...")

# 8-5. Cities:
def describe_city(city, country='Bangladesh'):
    """Print a simple sentence stating where the city is located."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('dhaka')
describe_city(city="noakhli")
describe_city(city='Reykjavik', country="iceland")


# Ex-3:
# formatted_name.py
def fromatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

name = fromatted_name('musfique', 'ahmed')
print(name)


def formatted_name(first_name, last_name, midle_name=''):
    """Return a full name, neatly formatted."""
    if midle_name:
        full_name = f"{first_name} {midle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

name = formatted_name('mushfi', 'ahmed', 'lee')
print(name)
name = formatted_name('mushfi', 'ahmed')
print(name)

# Or, 
def formatted_name(first_name, last_name, midle_name=''):
    """Return a full name, neatly formatted."""
    if midle_name:
        return f"{first_name} {midle_name} {last_name}"
    return f"{first_name} {last_name}"

name = formatted_name('mushfi', 'ahmed', 'lee')
print(name.title())
name = formatted_name('mushfi', 'ahmed')
print(name.title())


# Ex-4:
# person.py
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

info = build_person('musfique', 'ahmed')
print(info)

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

info = build_person('musfique', 'ahmed', 27)
print(info)
info = build_person('musfique', 'ahmed', age=27)
print(info)

# greeter.py
def fromatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print(f"\nPlease enter your name-\n(Enter 'q' to quit.)")

    f_name = input("Enter your first name: ")
    if f_name == 'q':
        break
    l_name = input("Enter your last name: ")
    if l_name == 'q':
        break

    name = fromatted_name(first_name=f_name, last_name=l_name)
    print(f"\nHello, {name}!")


## T I Y -
# 8-6. City Names:
def city_country(city, country):
    message = f"{city}, {country}"
    return message.title()

mess = city_country('santiago', 'chilie')
print(f"\"{mess}\"") ##** use print("\word\"") to print something with double qouts.


# 8-7 & 8-8. Album & User Album:
def make_album(artist_name, album_title, num_of_songs= None):
    album = {'artist': artist_name, 'title': album_title}
    if num_of_songs:
        album['songs'] = num_of_songs
    # print(album)
    return album

while True:
    print(f"\nPlease enter the informations about the album-")
    print("(Enter 'q' to quit.)")
    name = input("Enter artist name: ")
    if (name=='q'):
        break
    title = input("Enter the album title: ")
    if (title=='q'):
        break
    num = input("Enter the number of songs: ")
    if (num=='q'):
        break
    if num == "":
        info = make_album(artist_name=name, album_title=title)
    else:
        info = make_album(artist_name=name, album_title=title, num_of_songs=int(num))

    print(info)

# Or,
def make_album(artist_name, album_title, num_of_songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_of_songs:
        album['songs'] = num_of_songs
    # print(album)
    return album

while True:
    print(f"Please enter the informations about the album-")
    print("(Enter 'q' to quit.)")
    name = input("Enter artist name: ")
    title = input("Enter the album title: ")
    num = input("Enter the number of songs: ")
    if (name=='q') or (title=='q') or (num=='q'):
        break
    if num == "":
        info = make_album(artist_name=name, album_title=title)
    else:
        info = make_album(artist_name=name, album_title=title, num_of_songs=int(num))

    print(info)


# Ex - 5:
# GREET_USRE.py
def greet_user(users):
    """Print a siple greeting to each user in the list"""
    for user in users:
        msg = f"Hello {user.title()}."
        print(msg)
    
lst = ['anas', 'abu', 'usfique']
greet_user(lst)


# printing_models.py
# normal veersion-
unprinted_design = ['ohone case', 'robot pendant', 'dodecahedron']
printed_design = []
while unprinted_design:
    current_desing = unprinted_design.pop()
    print(f"Printing Model: {current_desing.title()}")
    printed_design.append(current_desing)

print(f"\nThe following models have been printed-")
for i in printed_design:
    print(i.title())

# Function version - 
def printing(unprinted, printed):
    while unprinted:
        current = unprinted.pop()
        print(f"Printing Model: {current.title()}")
        printed.append(current)

def printed(printed):
    print("\nThe following desings have been printed-")
    for design in printed:
        print(design.title())

unprinted_design = ['ohone case', 'robot pendant', 'dodecahedron']
printed_design = []

printing(unprinted=unprinted_design, printed=printed_design)
printed(printed=printed_design)

# printing_models.py
def printing(unprinted, printed):
    while unprinted:
        current = unprinted.pop()
        print(f"Printing Model: {current.title()}")
        printed.append(current)

def printed(printed):
    print("\nThe following desings have been printed-")
    for design in printed:
        print(design.title())

unprinted_design = ['ohone case', 'robot pendant', 'dodecahedron']
printed_design = []

printing(unprinted=unprinted_design[:], printed=printed_design)
printed(printed=printed_design)
print(unprinted_design)


## T I Y -
# 8-9. Messages:
def show_messages(mess):
    """Print each text message."""
    for i in mess:
        print(i.capitalize())
    
lst = ['hi', 'hello', 'bye', 'who are you?']
show_messages(lst)
# Or,
def show_messages(*mess):
    """Print each text message."""
    for i in mess:
        print(i.capitalize())
    
show_messages('hi', 'hello', 'bye', 'who are you?')

# 8-10. Sending Messages:
def send_messages(unsent, sent):
    """Print each text message."""
    while unsent:
        message = unsent.pop()
        print(message.capitalize())
        sent.append(message)

unsent_message = ['hi', 'hello', 'bye', 'who are you?']
sent_message = []
send_messages(unsent=unsent_message, sent=sent_message)

print(unsent_message)
print(sent_message)

# 8-11. Archived Messages:
def send_messages(unsent, sent):
    """Print each text message."""
    while unsent:
        message = unsent.pop()
        print(message.capitalize())
        sent.append(message)

unsent_message = ['hi', 'hello', 'bye', 'who are you?']
sent_message = []
send_messages(unsent=unsent_message[:], sent=sent_message)

print(unsent_message)
print(sent_message)


# Ex - 6:
# pizza.py
def make_pizza(*toppings): # (*) makes tuples.
    """Print the list of toppings."""
    print(toppings)
make_pizza('alu', 'peyaj', 'roshun', 'ada')
make_pizza('gajor')

# pizza.py
def make_pizza(*toppings): # (*) makes tuples.
    """Summarize the pizza."""
    print(f"\nMaking a pizza with following toppings:")
    for toppping in toppings:
        print(f" -{toppping.title()}")

make_pizza('alu', 'peyaj', 'roshun', 'ada')
make_pizza('gajor')

# pizza.py
def make_pizza(size, *toppings): # (*) makes tuples.
    """Summarize the pizza."""
    print(f"\nMaking a {size}-inch pizza with following toppings:")
    for toppping in toppings:
        print(f" -{toppping.title()}")

make_pizza(12, 'alu', 'peyaj', 'roshun', 'ada')
make_pizza(9, 'gajor')

# Ex - 7:
# user_profile.py
def build_profile(first, last, **user_info): #Arbitrary keyword arguments
    """Build a dictionary containing everyting we know about a user"""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_profile('naik','baik', 
                             location='uganda',
                             feild='Data Science')
print(user_profile)


## T I Y -
# 8-12. Sandwiches:
def make_sandwich(*items):
    """Print a summary of the Sandwich"""
    print(f"Making a Sandwich with following toppings- ")
    for item in items:
        print(f" - {item.capitalize()}")

make_sandwich('egg', 'tomato', 'beef', 'chezz', 'theze nuts')

# 8-13. User Profile:
# user_profile.py
def build_profile(first, last, **user_info): #Arbitrary keyword arguments
    """Build a dictionary containing everyting we know about a user"""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_profile('musfique','ahmed', 
                             location='mirpur, dhaka', 
                             degree='B.Sc', 
                             feild='Data Science', )
print(user_profile)
# Or, 
def build_profile(first, last, **user_info): #Arbitrary keyword arguments
    """Build a dictionary containing everyting we know about a user"""
    lst = list(user_info.items())
    lst.insert(0, ('first', first))
    lst.insert(1, ('last', last))
    user_info = dict(lst)
    return user_info

user_profile = build_profile('musfique', 'ahmed', 
                             location='mirpur, dhaka', 
                             degree='B.Sc', 
                             feild='Data Science', )
print(user_profile)

# 8-14. Cars:
def make_car(manufac, model, **other_info):
    """Print the dictionary with all the informations"""
    other_info['manufacturer'] = manufac
    other_info['model'] = model
    return other_info

car = make_car('subaru', 'outback', color='blue', two_package=True)
print(car)
# Or, 
def make_car(manufac, model, **other_info):
    """Print the dictionary with all the informations"""
    lst = list(other_info.items())
    lst.insert(0, ('manufacturer', manufac))
    lst.insert(1, ('model', model))
    other_info = dict(lst)
    return other_info

car = make_car('subaru', 'outback', color='blue', two_package=True)
print(car)
