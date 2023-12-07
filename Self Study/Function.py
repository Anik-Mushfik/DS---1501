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

