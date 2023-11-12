#1(b)- 
sum = 10
for i in range(1,4):
    sum = sum + 10
    for j in range(1,4):
        sum = sum + 20
        for k in range(1,4):
            sum = sum + 30
print("Total sum: " , sum)



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


#3(a)-
lst = [2,3,4,5,6,7,8]
print(lst[3:-3])
print(lst[:])
print(lst[:-3])
print(lst[-3:])


#3(b)-
unit=float(input("enter the consumed unit:"))

if unit<=50:
    Totall_Bill = (unit*0.50)
elif unit<=150:
     Totall_Bill = ((50*0.50)+(unit-50)*0.75)
elif unit<=250:
     Totall_Bill = ((50*0.50)+(100*0.75)+((unit-150)*1.20))
elif unit>250:
     Totall_Bill = ((50*0.50)+(100*0.75)+(100*1.20)+((unit-250)*1.50))

surcharge = Totall_Bill * 0.2
Bill = surcharge + Totall_Bill
print(Bill)


#3(c)-
message = "I love watching cricket, but quality our cricket should be improved."
i = message.find("cricket")
if i != -1:
    message = message.replace("cricket", "soccer")
    print(message)


