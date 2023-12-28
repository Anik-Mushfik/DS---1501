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


# Problem - 2:
def pattern_printing(num):
    """Prints a specific pattern based on the input"""
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

n = int(input("Enter the number: "))
pattern_printing(n)


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