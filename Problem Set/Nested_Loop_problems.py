# Problem - 1:
n = int(input())
for i in range(n):
    for j in range(1,n+1):
        print(j, end="")
    print()


# Problem - 2:
n = int(input())
for i in range(1,n+1):
    for j in range(i,i+n):
        print(j, end="")
    print()


# Problem - 3:
n = int(input())
for i in range(1,n+1):
    for j in range(i,i+i):
        print(j, end="")
    print()


# Problem - 4:
n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print('_', end="")
    for k in range(i):
        print(i, end="")
    print()


# Problem - 5:
n = int(input())
for i in range(n,0,-1):
    for j in range(n, (i-1), -1):
        print(j, end="")
    print()


# Problem - 6:
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()


# Problem - 7:
n = int(input())
for i in range(n):
    for j in range(n):
        print('*', end="")
    print()


# Problem - 8:
n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print('*', end="")
    print()


# Problem - 9:
n = int(input())
for i in range(n):
    if (i%2 == 0):
        for j in range(n):
            if (j%2 == 0):
                print(1, end="")
            else:
                print(0, end="")
    else:
        for j in range(n):
            if (j%2 == 0):
                print(0, end="")
            else:
                print(1, end="")
    print()


# Problem - 10:
n = int(input())
for i in range(1, n+1):
    for j in range(n-i):
        print('-', end="")
    for k in range(i):
        print('*', end="")
    print()


# Problem - 11:
n = int(input())
x = 0
for i in range(1,n+1):
    for j in range(n-i):
        print('_', end="")
    for k in range(i+x):
        print('*', end="")
    x = i
    print()

# Or, 
n = int(input())
for i in range(1, n+1):
    for j in range(n-i):
        print('_', end="")
    for k in range((2*i)-1):
        print('*', end="")
    print()


# Problem - 12:
num = int(input())
n = (num//2) + 1
for i in  range(1, n+1):
    for j in range((n)-i):
        print('_', end="")
    for k in range((2*i)-1):
        print('*', end="")
    print()
for x in range((n-1), 0, -1):
    for y in range(n-x):
        print('_', end="")
    for z in range((2*x)-1):
        print('*', end="")
    print()


# Problem - 13:
n = int(input())
for i in range(1, n+1):
    for x in range(1,i+1):
        print(x, end="")
    for y in range(((2*n)-((2*i)+1))):
        print('_', end="")
    for z in range(i, 0, -1):
        if z == n:
            continue
        print(z, end="")
    print()


# Problem - 14:
n = int(input())
for i in range(1, n+1):
    if (i%2 == 0):
        print('*', end="")
        for j in range(n-2):
            print('_', end="")
        print('*')
    else:
        for k in range(n):
            print('*', end="")
        print()


# Problem - 15:
n = int(input())

for i in range(n, 0, -1):
    if (i==1) or (i==n):
        for j in range(n):
            print('Z', end="")
        print()
    
    else:
        for x in range(1,i):
            print(' ', end="")
        print('Z')

# Or, GPT
def print_pattern(n):
    for i in range(1, n+1):
        # Print 'Z' for the first row and last column
        if i == n or i == 1:
            print('Z' * n)
        else:
            # Print spaces before 'Z'
            print(' ' * (n-i) + 'Z')

# Example usage with input 5
input_value = int(input("Enter a number: "))
print_pattern(input_value)


# Problem - 16:
n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i==j) or (j == (n+1)-i):
            print('*', end="")
        else:
            print('_', end="")
    print()

# Or, 
n = int(input())
for i in range(n):
    for j in range(n):
        if (i==j) or (j ==(n-1)-i):
            print('*', end="")
        else:
            print('_', end="")
    print()

# Co-pilot -
# Define the input
n = 7

# Loop through the rows
for i in range(n):
    # Loop through the columns
    for j in range(n):
        # Check if the row and column are equal or opposite
        if i == j or i == n - j - 1:
            # Print a star
            print("*", end="")
        else:
            # Print an underscore
            print("_", end="")
    # Print a new line
    print()

# Or, (Doesn't work with inputs more than 5)
n = int(input())
for i in range(1, n+1):
    if (i==1) or (i==n):
        for j in range(1,n+1):
            if (j==1) or (j==n):
                print('*', end="")
            else:
                print('_', end="")
    else:
        for j in range(1,n+1):
            if (j==1) or (j==n):
                print('_', end="")
            elif (i%2 == 0):
                if (j%2 == 0):
                    print('*', end="")
                else:
                    print('_', end="")
            else:
                if (j%2 != 0):
                    print('*', end="")
                else:
                    print('_', end="")

    print()


# Problem - 17:
n = int(input())
x = (n//2)+1
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i == x) or (j == x):
            print('$', end="")
        elif (j == x-(i-1)) or (j == x+(i-1)) or (j == x-(n-i)) or (j == x+(n-i)):
            print('$', end="")
        else:
            print('_', end="")
    print()

# Or,



# Problem - 18:
n = int(input())
for i in range(1,n+1):
    if (i == (n//2)+1):
        for j in range(n):
            print("H",end=" ")
    else:
        for j in range(1, n+1):
            if (j==1) or (j==n):
                print('H', end=" ")
            else:
                print(' ', end=" ")
    print()



# Python code to print a dollar pattern
# Input: 13
# Output:
# $_____$_____$
# _$____$____$_
# __$___$___$__
# ___$__$__$___
# ____$_$_$____
# _____$$$_____
# $$$$$$$$$$$$$
# _____$$$_____
# ____$_$_$____
# ___$__$__$___
# __$___$___$__
# _$____$____$_
# $_____$_____$

# Define the input
n = 13

# Loop through the rows
for i in range(n):
    # Loop through the columns
    for j in range(n):
        # Check if the row and column are equal or opposite
        if i == j or i == n - j - 1:
            # Print a dollar
            print("$", end="")
        # Check if the row or column is the middle one
        elif i == n // 2 or j == n // 2:
            # Print a dollar
            print("$", end="")
        else:
            # Print an underscore
            print("_", end="")
    # Print a new line
    print()
