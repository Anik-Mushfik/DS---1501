#list in list
lis_1 = [5,10,15,20,25,30,35,40]
lis_1[3] = 200
print(lis_1)

motorcycles = ['bmw', 'suzuki', ['kawasaki', 'honda'], 'toyota']
motorcycles.reverse()
print(motorcycles)
motorcycles.reverse()
print(motorcycles[2][1])
motorcycles[2].remove('honda')

#10/25/2023 CT
#Qus-3:
list = []
print(f"Enter your numbers: (Enter 'f' when you are done.)")
choices = 0
while choices != 'f':
    choice = input()
    list.append(choice)
    choices = choice
else:
    list.pop()
    print(list)
if len(list) == 1:
    print("Not gonna work")
else:
    odd = 0
    even = 0
    for x in list:
        indx = list.index(x)
        if indx%2 == 0 and indx>0:
            even += int(x)
        elif indx == 0:
            even+= int(x)
        else:
            odd += int(x)
    print(f"Sum of odd index:{odd}")
    print(f"Sum of even index:{even}")

#Or,
a = []
n = int(input("ENTER NUMBER OF ELEMENTS : "))
for i in range (n):
    a.append(input("ENTER ELEMENT : "))
print(a)
odd = 0
even = 0
for x in a:
    if n != 1 :
        indx = a.index(x)
        if indx%2 == 0 and indx>0:
            even += int(x)
        elif indx == 0:
            even+= int(x)
        else:
            odd += int(x)
        print(odd)
        print(even)
    else:
        print("Not gonna work")



#Sakharyui sir ct
'''
In the computer labs of UIU, 35 students can sit together for classes. Write a program in python,
that will take the number of students admitted in the first trimester of data science program. As the
students are taking admissions one-by-one, the department has decided to fill up the open sections
full to their capacity and then open a new section. For example, if 90 students are admitted, 3
sections will be needed. First section will be full first, 35 students then second section will be full
with another 35 students and the last section will have only 20 students. Your program will print
will be needed for these newly admitted students and the size of the last section.
'''

num = int(input("Enter the number of admitted students: "))
if num % 35 ==0:
    print(f"For {num} newly admitted students {(num // 35)} sections will be needed and the size of the last section is 35 students.")
else:
    print(f"For {num} newly admitted students {(num // 35) + 1} sections will be needed and the size of the last section is {num % 35} students.")
