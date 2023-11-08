#1-(c)
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