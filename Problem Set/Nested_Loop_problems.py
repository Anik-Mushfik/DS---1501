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
