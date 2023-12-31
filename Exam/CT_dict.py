vote_dict = {
    'Messi' : ['Haaland', 'Mbappe', 'Neymar'],
    'Neymar' : ['Messi', 'Mbappe', 'Haaland'],
    'Mbappe' : ['Messi', 'Haaland', 'Neymar'],
    'Haaland' : ['Messi', 'Mbappe', 'Neymar'],
    'KDB' : ['Messi', 'Mbappe', 'Haaland'],
    'Lewandovoski' : ['Messi', 'Mbappe', 'Haaland'],
}
votes = []
for i in vote_dict.values():
    for j in i:
        if j not in votes:
            votes.append(j)

print(len(votes))

for i in vote_dict.values():
    for j in i:
        votes.append(j)

print(len(set(votes)))

count = {"messi": 0, "neymar": 0, "mbappe":0, "haaland":0}
for y in vote_dict.values():
    for z in y:
        if z.lower() == "messi":
            count['messi'] += 1
        elif z.lower() == "neymar":
            count['neymar'] += 1
        elif z.lower() == "mbappe":
            count['mbappe'] += 1
        elif z.lower() == "haaland":
            count['haaland'] += 1

print(count)

maxi = count['messi']
m_vote = "messi"
for k, v in count.items():
    if v>maxi:
        maxi = v
        m_vote = k

print(f"{m_vote} got max votes")

max_lst = []
maxi = max(count.values())
for k, v in count.items():
    if v==maxi:
        max_lst.append(k)

print(*max_lst, sep=" and ",)
print(f"got max votes.", end="")

print("\nMax votes:")
for pla in max_lst:
    print(pla.title())