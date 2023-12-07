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
