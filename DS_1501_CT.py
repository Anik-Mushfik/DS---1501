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
    print("Balda diso amar")
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
