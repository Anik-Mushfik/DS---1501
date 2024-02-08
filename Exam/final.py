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
        
