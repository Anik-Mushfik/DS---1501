# Problem - 1:
n = int(input())
for i in range(1, n):
    print(i, end=", ")
print(n)
# Or,
print([i for i in range(1, int(input())+1)])
# Or,
print(*[i for i in range(1, int(input())+1)])
# Or,
n = int(input())
num = []
for i in range(1, n+1):
    num.append(i)
    num.append(',')
num.pop()
print(*num)


# Problem - 2:
n = int(input())
count = 0
x = 1
while True:
    if count == (n-1):
        break
    else:
        print(x, end=", ")
        x += 2
        count += 1
print(x)


# Problem - 3:
n = int(input())
for i in range(1,n+1):
    if i == n:
        if  (i%2 != 0):
            print(1)
        else:
            print(0)
    elif (i%2 != 0):
        print(1, end=", ")
    else:
        print(0, end=", ")


# Problem - 5:
x = int(input())
y = int(input())
while x != y:
    if x<y:
        print((x**2), end=", ")
        x += 1
    if x>y:
        print((x**2), end=", ")
        x -= 1
print("Reached!")


# Problem - 6:
num = int(input("Enter the number: "))
n = int(input("How many tries?: "))
player1_win = True

for i in range(n,0,-1):
    gusse  = int(input())
    if num == gusse:
        player1_win = False
        break
    else:
        print(f"Wrong, {i-1} Choice(s) Left!")

if player1_win:
    print(f"Player-1 wins!")
else:
    print(f"Right, Player-2 wins!")


# Problem - 9:
n = int(input())
grades = []

for i in range(n):
    marks = list(map(float, input().split()))
    a = marks[0]
    hw = marks[1]
    ct = marks[2]
    mt = marks[3]
    tf = marks[4]

    mt = (mt/50)*30
    tf = (tf/100)*40

    total = a + hw + ct + mt + tf

    if (90 <= total <= 100):
        grade = "A"
    elif (86 <= total <= 89):
        grade = "A-"
    elif (82 <= total <= 85):
        grade = "B+"
    elif (78 <= total <= 81):
        grade = "B"
    elif (74 <= total <= 77):
        grade = "B-"
    elif (70 <= total <= 73):
        grade = "C+"
    elif (66 <= total <= 69):
        grade = "C"
    elif (62 <= total <= 65):
        grade = "C-"
    elif (58 <= total <= 61):
        grade = "D+"
    elif (55 <= total <= 57):
        grade = "D"
    elif (0 <= total < 55):
        grade = "F"

    grades.append(grade)

for gra in grades:
    no = grades.index(gra) + 1
    print(f"Student {no}: {gra}")
