# Qus - 1:
def fuactorial(n):
    """Print the value of n! in the output"""
    fact = 1
    for i in range(1, (n+1)):
        fact *= i
    return fact

num = int(input())
factor = fuactorial(num)
print(factor)


# Qus - 3:
def calculate_sum(*lst):
    """Print the sum of the numbers coming from the console"""
    sum = 0
    for i in lst:
        sum += i
    return sum

total = calculate_sum(100, -100)
print(total)

# Or, 
def calculate_sum(list):
    """Print the sum of the numbers coming from the console"""
    total = sum(list)
    print(f"Sum in function: {total}")

lst = list(map(int, input().split()))
calculate_sum(lst)
print(f"Sum in main: {sum(lst)}")