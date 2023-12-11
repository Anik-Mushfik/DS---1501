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


# Problem - 5:
def swap(a, b):
    """Swap two numbers(Pass by value)"""
    a,b = b,a
    print(f"Value in func: {a} {b}")
    return a,b

lst = list(map(int, input().split()))
sp = swap(lst[0], lst[1])
print(f"Value in main: {lst[0]} {lst[1]}")
# Or,
def swap(a, b):
    """Swap two numbers(Pass by value)"""
    a,b = b,a
    print(f"Value in func: {a} {b}")
    return a,b

num1 = int(input())
num2 = int(input())
sp = swap(num1, num2)
print(f"Value in main: {num1} {num2}")


# Problem - 6:
def swap2(lst):
    """Swap two numbers(Pass by reference or, 
    "pass by object reference" or, 
    "pass by assignment.")"""
    lst[0], lst[1] = lst[1], lst[0]
    print(f"Value in func: {lst[0]} {lst[1]}")
    return lst

in_lst = list(map(int, input().split()))
out = swap2(in_lst)
print(f"Value in main: {in_lst[0]} {in_lst[1]}")


# Problem - 7:
def even_num(lst):
    """Determine only even numbers in an array of input integers"""
    even = []
    for i in lst:
        if i%2 == 0:
          even.append(i)
    return even

in_lst = list(map(int, input().split()))
out = even_num(in_lst)
print(*out)


# Problem - 8:
def min_value(lst):
    """Find and return the minimum value in a list"""
    val = min(lst)
    return val

in_lst = list(map(int, input().split()))
out = min_value(in_lst)
print(f"Minimum Value: {out}")
# Or, 
def min_value(lst):
    """Find and return the minimum value in a list"""
    val = lst[0]
    for i in lst:
        if i < val:
            val = i
    return val

in_lst = list(map(int, input().split()))
out = min_value(in_lst)
print(f"Minimum Value: {out}")


