##Printing from a dictionary -
# human = {'name': 'rubayet', 'gender': 'male', 'age': 25}
# print(human['age'])

##Adding to a dictionary - 
# human = {}
# human['dept'] = 'CSE'
# human['profession'] = 'student'
# print(human)

##Deleting an item - 
# del human['dept']
# print(human)

##Using for loop in a dictionary - 
favorite_lan = {'miti': 'python', 'raufur': 'c', 'anas': 'rubi', 'inan': 'python', 'sakib': 'java'}
# print(f"Favorite language of Miti is {favorite_lan['miti'].title()}")
# for key, value in favorite_lan.items():
#     print("Key: " + key + " , " + " Value: " + value)

##Printing only keys or values - 
# for key in favorite_lan.keys():
#     print("Key: " + key)
# for value in favorite_lan.values():
#     print("Value: " + value)

##Sorting dictionary - 
# for k in sorted(favorite_lan.keys()):
#     print("Key: " + k)
# for v in sorted(favorite_lan.values()):
#     print("Value: " + v)

##Not reapiting a value multiple times:
# for v in set(favorite_lan.values()):
#     print("Value: " + v)

