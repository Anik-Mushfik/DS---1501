#1-(c)-
str = "Data Science, United International University."
listofwords = []
word = ""
count = 0
for c in str:
    if c == " ":
        count += 1
        listofwords.append(word)
        word = ""
    else:
        word += c
listofwords.append(word)
print(count)
word = ""
for w in listofwords:
    word = word+w[0]
print(word)


#2(a)-
listA = [4,6,-3,-4,2,6]
sum = 0
for i in listA:
    if i < 0:
        sum += i
print(sum)


#2(b)-
listCountries = ["Bangladesh", "India", "Pakistan", "Srilanka", "Afganistan"]
listcapitals = ["Dhaka", "Delhi", "Islamad", "Colombo", "Kabul"]
user_input = input()
if user_input in listCountries:
    i = listCountries.index(user_input)
    print(listcapitals[i])
else:
    print("Unknown")


#2(c)-
listNum = [4,5,-7,41,3,17,2]
maxi = listNum[0]
for i in listNum:#Vul = range(1,len(listNum)):
    if i > maxi:
        maxi = i
print(maxi)


#3(c)-
message = "I love watching cricket, but quality our cricket should be improved."
i = message.find("cricket")
if i != -1:
    message = message.replace("cricket", "soccer")
    print(message)


