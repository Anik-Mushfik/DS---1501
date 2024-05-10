## Answer No: 1
# (a):
upozilla_map = {
    "Dighinala": ['Panchari', 'Khagrachari'], 
    "Panchari": ['Khagrachari', 'Dighinala', 'Mati Ranga'], 
    "Khagrachari": ['Dighinala', 'Panchari', 'Mati Ranga', 'Ramgarh', 'Mohla Chari'], 
    "Mati Ranga": ['Panchari', 'Khagrachari', 'Ramgarh'], 
    "Ramgarh": ['Mati Ranga', 'Khagrachari', 'Mohal Chari', 'Lakshmichari', 'Manikchari'], 
    "Mohla Chari": ['Khagrachari', 'Ramgarh', 'Lakshmichari'], 
    "Manikchari": ['Ramgarh', 'Lakshmichari'], 
    "Lakshmichari": ['Manikchari', 'Ramgarh', 'Mohal Chari'], 
}

# (b):
lst = [len(x) for x in upozilla_map.values()]
maxi = max(lst)
mini = min(lst)

max_neigh = []
min_neigh = []

for upozilla, neighbor in upozilla_map.items():
    neigh_num = len(neighbor)
    print(f"{upozilla} has {neigh_num} neighbors.")
    if neigh_num == maxi:
        max_neigh.append(upozilla)
    if neigh_num == mini:
        min_neigh.append(upozilla)

print(f"Upozillas with maximum neighbours: \n=>", end="")
print(*max_neigh, sep="\n=>")
print(f"Upozillas with minimum neighbours: \n=>", end="")
print(*min_neigh, sep="\n=>")

## Answer: 2
# (a):
def evenSum(x,y):
    """Find the even numbers in the range of (x-y) 
    and return the sum of those even numbers."""
    sum = 0
    for i in range(x, y+1):
        if i % 2 == 0:
            sum += i

    return sum

print(evenSum(1,10))


# (b):








# 4 = >
f = open("source.txt","r")
content = f.readlines()

for i in content:
    i.split(" ")
    #print(i)
    content = i

low = content.lower()
spl = low.split()

v_lst = []
for j in spl:
   
    if j[0] == "a" or j[0] == "e" or j[0] == "i" or j[0] == "o" or j[0] == "u":
        v_lst.append(j)

print(v_lst)

finalString = " "
for k in v_lst:
    if k == v_lst[-1]:
        finalString += f"{k}."
    else:
        finalString += f"{k}, "

print(finalString)
f.close()

w = open("desh.txt","w")
w.write(finalString)
w.close()