info = {'personal_data':
            {'name': 'Lauren',
            'age': 20,
            'major': 'Information Science',
            'physical_features':
                {'color':
                    {'eye': 'blue',
                    'hair': 'brown'
                    },
                'height': "5.8"}
                },
        'other':
            {'favorite_colors': ['purple', 'green', 'blue', 'indigo'],
            'interested_in': ['social media', 'intellectual property','copyright', 'music', 'books']
            }
        }

# Qus-1:
print(info['personal_data']['physical_features']['color']['eye'])
# Or,
for k, v in info['personal_data']['physical_features']['color'].items():
    if k == 'eye':
        print(f"{v}")

# Qus-2:
for k, v in info['personal_data']['physical_features'].items():
    if k == 'height':
        print(v)
        if float(v) > 5:
            print(True)
        else:
            print(False)

# Qus-3:
favorite_colors = info['other']['favorite_colors']

for color in favorite_colors:
    if color[0] in ['a', 'e', 'i', 'o', 'u']:
        print(color.title())

#Qus-4:
count = 0
print(f"Areas of interests:")

for i in info['other']['interested_in']:
    print(f"\t{i.capitalize()}")
    count += 1
print(f"Number of areas: {count}")

#Qus-5:
interested = False
for i in info['other']['interested_in']:
    if i == 'gadgets':
        interested = True
        break
if interested:
    print(f"Yes, this person has interest in gadgets.")
else:
    print(f"No, this person doesn't has any interest in gadgets.")
