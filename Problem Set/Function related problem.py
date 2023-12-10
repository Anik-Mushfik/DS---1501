# Problem - 1:
def print_message():
    """Print a custom message"""
    print(f"This is a function")

print_message()


# Problem - 2:
def print_input(val):
    """Print an input character value"""
    print(f"Value received from main: {val}")

value = input()
print_input(value)


# Problem - 3:
def calculate_sum(*lst):
    """Calculate the sum of n numbers"""
    total = sum(lst)
    print(f"Sum In Function: {total}")
    return total

sumation = calculate_sum(100, -100)
print(f"Sum In Main: {sumation}")
# Or,
def calculate_sum(*lst):
    """Calculate the sum of n numbers"""
    total = 0
    for i in lst:
        total += i
    print(f"Sum In Function: {total}")
    return total

sumation = calculate_sum(80, 33, 27)
print(f"Sum In Main: {sumation}")


# Problem - 4:
def calculate_sum(lst0):
    """calculate the sum of n numbers 
    coming from the console and stored in an array"""
    total = sum(lst0)
    print(f"Sum In Function: {total}")
    return total

lst = list(map(int, input().split()))
sumation = calculate_sum(lst)
print(f"Sum In Main: {sumation}")
# Or, 
def calculate_sum(lst0):
    """calculate the sum of n numbers 
    coming from the console and stored in an array"""
    total = 0
    for i in lst0:
        total += i
    print(f"Sum In Function: {total}")
    return total

lst = []
num = int(input("Enter the number of values to sum: "))
for i in range(num):
    val = int(input("Enter a number: "))
    lst.append(val)

sumation = calculate_sum(lst)
print(f"Sum In Main: {sumation}")


