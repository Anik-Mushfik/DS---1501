audidences=['raian','fahad','sakib','mamun','mim', 'raisa','ripon']

icc_champion_pred={
    'raian':'india',
    'fahad':'england',
    'mamun':'india',
    'ripon':'australia'
}

for i in icc_champion_pred.keys():
    index = audidences.index(i)
    name = audidences.pop(index)
    print(f"Thanks {name} for taking the poll.")
print(audidences)
print(*[f"\nHi {v}, please take the poll."for v in audidences])