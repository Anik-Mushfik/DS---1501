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


# Problem - 4:
n = int(input())
num = list(map(float, input().split()))
avarage = sum(num) / n
print(f"AVG of {n} inputs: {round(avarage,6)}") # round(number, joto ghor nibe toto)
# Or,
n = int(input())
sum = 0
for i in range(n):
    num = float(input())
    sum += num
avarage = sum / n
print(f"AVG of {n} inputs: {round(avarage,6)}")
# Or, (Mahi) - 
num = int(input())
total = 0
for i in range(num):
	total += float(input())
avg = f"{total/num :.6f}" # number :.(joto ghor nibe toto)f
print(f"AVG of {num} input: {avg}")


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


# Problem - 7:
count = 1
while True:
    user = input()
    if user == 'A':
        break
    else:
        print(f"Input {count}: {user}")
        count += 1
# Or,
out = []
while True:
    user = input()
    if user == 'A':
        break
    else:
        out.append(user)

for i in out:
    no = out.index(i) + 1
    print(f"Input {no}: {i}")


# Problem - 8:
user_input = int(input())
user = str(user_input)
for i in reversed(user):
    print(i, end="")
# Or,
# Get user input for an integer
number = int(input("Enter an integer: "))

# Initialize variables
reversed_number = 0
original_number = abs(number)  # To handle negative numbers

# Reverse the digits using a loop
while original_number > 0:
    digit = original_number % 10
    reversed_number = reversed_number * 10 + digit
    original_number = original_number // 10

# If the input number was negative, make the reversed number negative
if number < 0:
    reversed_number *= -1

# Print the reversed integer
print(f"Reversed integer: {reversed_number}")


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


# Problem - 11:
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += (i**2)*(i+1)
print(f"Result: {sum}")


# Problem - 12:
n = int(input())
x = 1
y = 1
a = 0
print(x, end=", ")
for i in range(n-2):
    print(x, end=", ")
    a = x
    x += y
    y = a
print(x)
# Or, (Nafiz)
n = int(input())
a, b = 0, 1  
for i in range(n-1): 
    print(b, end=", ") 
    a, b = b, a + b #coma dile eki time a ekshathe change hobe
print(b)


# Problem - 13:
n = int(input())

num = []
fac = 1
for i in range(n,0,-1):
    fac *= i
    num.append(i)
    num.append('X')
num.pop()

print(f"{n}! =", end=" ")
print(*num, end=" ")
print(f"= {fac}")


# Problem - 14:
n = int(input())
r = int(input())
x = n-r

fac = 1
for i in range(1,n+1):
    fac *= i
fac_n = fac

fac = 1
for i in range(1,r+1):
    fac *= i
fac_r = fac

fac = 1
for i in range(1,x+1):
    fac *= i
fac_x = fac

n_c_r = fac_n / (fac_r * fac_x)
print(int(n_c_r))
# Or, 
n=int(input())
r=int(input())

n_fact,r_fact,x_fact=1,1,1
for i in range(n,0,-1):
    n_fact*=i
    
for j in range(r,0,-1):
    r_fact*=j
    
for k in range((n-r),0,-1):
    x_fact*=k
    
print(f"nCr= {(n_fact/(r_fact*x_fact))}")


# Problem - 15:
x = int(input())
y = int(input())
print(x**y)
# Or,
user = list(map(int, input().split()))
x = user[0]
y = user[1]
print(x**y)


# Problem - 16:
n1 = int(input())
n2 = int(input())
## GCD - 
gcd_n1 = [1,n1]
gcd_n2 = [1,n2]

for i in range(2,((n1//2)+1)):
    if n1%i == 0:
        gcd_n1.append(i)
for j in range(2,((n2//2)+1)):
    if n2%j == 0:
        gcd_n2.append(j)

for x in sorted(gcd_n1):
    if x in gcd_n2:
        pri = x
print(f"GCD: {pri}")
## LCM -
c = n1
while True:
    if (c % n1 == 0) and (c % n2 == 0):
        print(f"LSM: {c}")
        break
    c += 1
# Or,
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
##GCD
divisors_num2 = []
divisors_num1 = []
for x in range(1, num1+1):
    if (num1 % x == 0):
        divisors_num1.append(x)
for y in range(1, num2+1):
    if (num2 % y == 0):
        divisors_num2.append(y)
gcd = 0
for z in divisors_num1:
    if (z in divisors_num2) and (z > gcd):
        gcd = z
print(f"GCD: {gcd}")
##LCM
count = 1
while 1==1:
    if (count % num1 == 0.0) and (count % num2 == 0.0):
        #lcm = count
        print(f"LCM: {count}")
        break
    count += 1
# Or, (Mahi)-
one=int(input())
two=int(input())

one_div=[]
two_div=[]
common_div=[]
for x in range(1,one+1):
	if one % x == 0:
		one_div.append(x)
		
for y in range(1,two+1):
	if two % y == 0:
			two_div.append(y)

for x in one_div:
	if x in two_div:
		common_div.append(x)

gcd=max(common_div)
lcm=int((one*two)/gcd)

print(f"GCD: {gcd}")
print(f"LCM: {lcm}")


# Problem - 17:
n = int(input("Enter the number: "))
if (n == 1):
    is_prime = False
else:
	is_prime = True
for i in range(2,(n//2)+1):
    if (n%i == 0):
        is_prime = False
        break
if is_prime:
    print("Prime")
else:
    print("Not prime")

