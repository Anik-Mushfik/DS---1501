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

def describe_pet(pet_name, animal_type= 'dog'):
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

def build_person(first_name, last_name, age= None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

info = build_person('musfique', 'ahmed', 27)
print(info)
info = build_person('musfique', 'ahmed', age= 27)
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
def make_album(artist_name, album_title, num_of_songs= None):
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