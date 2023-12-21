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


# Problem - 9:
def list_multiply(lst0):
    """Multiplies the array elements by 2 and returns the array."""
    lst2 = []
    for i in lst0:
        lst2.append(i*2)
    return lst2

in_lst = list(map(int, input("Enter your list:\n").split()))
print(f"Multiplied list:")
print(*list_multiply(in_lst))

# Or, #A list changes parmanently even if you modify it in a function.
def list_multiply(lst0):
    """Multiplies the array elements by 2 and returns the array."""
    for i in range(len(lst0)):
        lst0[i] = lst0[i] *2

lst1 = list(map(int, input("Enter your list:\n").split()))
list_multiply(lst1)
print(f"Multiplied list:")
print(*lst1)


# Problem - 10:
def acsending_list(lst):
    """Sort and return an input array in ascending order"""
    return sorted(lst)

lst1 = list(map(int, input("Enter your list:\n").split()))
out = acsending_list(lst1)
print(f"List in ascending order:")
print(*out)
# Or, 
def acsending_list(lst):
    """Sort and return an input array in ascending order"""
    lst2 = []
    while lst:
        x = min(lst)
        lst2.append(x)
        lst.remove(x)
    return lst2

lst1 = list(map(int, input("Enter your list:\n").split()))
out = acsending_list(lst1)
print(f"List in ascending order:")
print(*out)


# Problem - 11:
def isPrime(n):
    """Determine whether a number is prime or not"""
    if n < 2: #jodi eta hoye jaye taile false diye dibe
        return False
    for i in range(2,((n//2)+1)): #uporer ta na hoile then eta dekhbe eta hoile false dibe
        if n%i == 0:
            return False
    return True #uporer konotai na hoile then eta dekhbe and true dibe

print(isPrime(169))


# Problem - 12:
def isPrime(n):
    """Determine whether a number is prime or not"""
    if n < 2: #jodi eta hoye jaye taile false diye dibe
        return False
    for i in range(2,((n//2)+1)): #uporer ta na hoile then eta dekhbe eta hoile false dibe
        if n%i == 0:
            return False
    return True #uporer konotai na hoile then eta dekhbe and true dibe

def allNum(num):
    """Iterate all the numbers until """
    primes = []
    for i in range(2,num):
        x = isPrime(i)
        if x:
            primes.append(i)
    return primes

in_num = int(input("Enter the number: "))
out = allNum(in_num)
print(f"Prime less than {in_num}: ",end="")
print(*out, sep=",")
# Or, (siam)
def siam(n):
	if n<2:
		return False
	for x in range(2,n):
		if n%x==0:
			return False
	return True
def general(low,high):
	prime=[i for i in range(low,high+1) if siam(i)]
	return prime
    		
print(general(2,10))


# Problem - 13:
# Testing-
def GenNthPrime(n):
    """Compute the Nth prime number"""
    lst = []
    if n<2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, ((n//2)+1)):
            if n%i == 0:
                is_prime = False
                break

    if is_prime:
        lst2.append(n)
        print(lst2)
        lst.append(n)
        print(lst)
    return lst
    
def allnum(num):
    """Provide all needed number to the function"""
    x = 0
    while len(lst2) < num:
        print(len(lst2))
        x += 1
        print(f"x={x}")
        GenNthPrime(x)
        
lst2 = []
in_num = allnum(5)
print(lst2)

# Actual Programme:
def GenNthPrime(n):
    """Compute the Nth prime number"""
    if n<2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, ((n//2)+1)):
            if n%i == 0:
                is_prime = False
                break

    if is_prime:
        lst2.append(n)
 
def all_num(num):
    """Provide all needed number to the function"""
    x = 0
    while len(lst2) < num:
        x += 1
        GenNthPrime(x)
    return x
   
lst2 = []
user_num = int(input("Enter a number: "))
in_num = all_num(user_num)
print(f"{user_num}th Prime: {in_num}")


#Or, Chat gpt-
def is_prime(num):
    # Function to check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def GenNthPrime(N):
    # Function to compute the Nth prime number
    if N <= 0:
        return "Invalid input. N should be a positive integer."
    
    prime_count = 0
    num = 2
    
    while True:
        if is_prime(num):
            prime_count += 1
            if prime_count == N:
                return num
        num += 1

# Example usage
N = int(input("Enter the value of N: "))
result = GenNthPrime(N)
print(f"The {N}th prime number is: {result}")


# Problem - 14:
def Calc_Std_deviation(array, num_of_elem):
    total = 0
    for i in array:
        x = (i-mean)**2
        total += x
    div = total/num_of_elem
    std_dev = div**(0.5)
    return round(std_dev,2)

def CalcMean(array, num_of_elem):
    mean = sum(array)/ num_of_elem
    return mean

def TakeInput():
    lst = input("Enter the numbers:\n").split()
    lst1 = [int(x) for x in lst]
    return lst1

data = TakeInput()
num = len(data)
mean = CalcMean(array=data, num_of_elem=num)
S_d = Calc_Std_deviation(array=data, num_of_elem=num)
print(f"Standard Deviation of the numbers: {S_d}")

# Or,
def distance_square(n):
    des = mean - n
    sqr = des**2
    return sqr

def summation(lst):
    """Sum of the square of its distance to the mean"""
    total = 0
    sqr = 0
    for i in lst:
        sqr = distance_square(i)
        total += sqr
    return total

def Standered_derivation(list_data):
    sumat = summation(data)
    gor = sumat/ len(data)
    alpha = gor**(0.5)
    return round(alpha,2)
    
data = list(map(int, input().split()))
mean = sum(data)/len(data)
stan_derv = Standered_derivation(data)
print(stan_derv) 

# Or,
def distance_square(n):
    des = mean - n
    sqr = des**2
    return sqr

def summation(lst):
    """Sum of the square of its distance to the mean"""
    total = 0
    sqr = 0
    for i in lst:
        sqr = distance_square(i)
        total += sqr
    return total

data = list(map(int, input().split()))
mean = sum(data)/len(data)
sumat = summation(data)
gor = sumat/ len(data)
alpha = gor**(0.5)
print(round(alpha,2))

# Testing - 
def distance_square(n):
    des = mean - n
    sqr = des**2
    return sqr

def summation(lst):
    """Sum of the square of its distance to the mean"""
    total = 0
    sqr = 0
    for i in lst:
        sqr = distance_square(i)
        total += sqr
    
        print(f"Total: {total}")
        print(f"Square: {sqr}")
    return total

#data = list(map(int, input().split()))
data = [4, 5, 5, 4, 4, 2, 2, 6]
mean = sum(data)/len(data)
print(mean)
sumat = summation(data)#13.9392
print(sumat)
gor = sumat/ len(data)
print(gor)#1.7424
alpha = gor**(0.5)
print(alpha)#1.32


# Problem - 15
def find_substr(a, b):
    """Find out if string 'b' is found anywhere in string 'a' or not"""
    if b in a:
        return 1
    else:
        return 0

in_user = input().split()
lst = [x for x in in_user]
out = find_substr(a=lst[0], b=lst[1])
print(out)


# Problem - 16:
def find_substr(a, b):
    """Find out if string 'b' is found anywhere in string 'a' or not"""
    if b in a:
        return 1
    else:
        return 0

def str_length(string):
    """Determine the lengths of the strings"""
    count = 0
    for i in string:
        count += 1
    return count

in_user = input().split()
lst = [x for x in in_user]
lenth1 = str_length(lst[0])
lenth2 = str_length(lst[1])

if lenth1 > lenth2:
    out = find_substr(a=lst[0], b=lst[1])
else:
    out = find_substr(a=lst[1], b=lst[0])
print(out)

# Or, (mahi)
def str_len(mahi):
	count = 0
	for letter in mahi:
		count += 1
	return count

def find_subtr(a,b):
	if str_len(b) > str_len(a):
		b,a = a,b
	if b in a:
		print("1")
	else:
		print("0")
		
a = input()
b = input()

find_subtr(a,b)


# Problem - 17:
def devisor(n):
    lst = [1,n]
    for i in range(2,(n//2)+1):
        if n%i == 0:
            lst.append(i)
    return lst

lst = list(map(int, input().split()))
n1_lst = devisor(lst[0])
n2_lst = devisor(lst[1])

def gcd(lst1, lst2):
    common = []
    for i in lst1:
        if i in lst2:
            common.append(i)
    return max(common)

gratest_cd = gcd(n1_lst, n2_lst)
print(f"GCD: {gratest_cd}")

lcm = (lst[0]*lst[1]) // gratest_cd
print(f"LCM: {lcm}")


# Problem - 18:
def ScalarMultiply(matri, n):
    """Multiply the matrix with the inputed number."""
    print(f"Multiplied by {n}:")
    for i in matri:
        for j in i:
            x = j*n
            print(x, end="\t")
        print()

def ShowMatrix(mat):
    """Disply the original matrix"""
    print(f"Original:")
    for i in mat:
        for j in i:
            print(j, end="\t")
        print()

def InputMatrix():
    """Take inupt for the matrix from the user"""
    for i in range(3):
        user_input = input().split()
        lst = [int(x) for x in user_input]
        matrix.append(lst)
    
matrix = []

first_call = InputMatrix()

num = int(input("\n"))

diplay = ShowMatrix(matrix)
multiply = ScalarMultiply(matri=matrix, n=num)


# Problem - 19:
def ScalarMultiply(matri, n):
    """Multiply the matrix with the inputed number."""
    print(f"\nMultiplied by {n}:")
    for i in matri:
        for j in i:
            x = j*n
            print(x, end="\t")
        print()

def ShowMatrix(mat):
    """Disply the original matrix"""
    print(f"\nOriginal:")
    for i in mat:
        for j in i:
            print(j, end="\t")
        print()

def InputMatrix(row_num, column_num):
    """Take inupt for the matrix from the user"""
    print(f"\nEnter the matrix:")
    for i in range(row_num):
        user_input = input().split()
        lst = [int(x) for x in user_input]
        if len(lst) != column_num:
            print("Input Error! Rerun the program!!!")
        matrix.append(lst)
    
matrix = []
lst = list(map(int, input("Enter the dimention of the matrix: (Row Column)\n").split()))

row = lst[0]
column = lst[1]

first_call = InputMatrix(row_num=row, column_num=column)

num = int(input("\nMultiply by:\n"))

diplay = ShowMatrix(matrix)
multiply = ScalarMultiply(matri=matrix, n=num)

# Problem - 20:


def Convert_Number (N, B):
    """Does the conversion"""


def Get_Number_And_Base ():
    """Takes number to be converted (N) and base value (B) 
    from user. Base must be between 2 and 16."""
    lst = list(map(int, input().split()))
    num = lst[0]
    if (2< lst[2] <16):
        base = lst[1]
    else:
        print(f"Base not within proper range!")
    return Convert_Number(N=num, B=base)


out = Get_Number_And_Base()