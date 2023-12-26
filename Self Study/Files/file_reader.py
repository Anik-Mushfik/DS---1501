# read--> r
# write--> w
# append--> a

file = open('D:/Python Study/DS---1501/Self Study/Files/message.txt', 'r')
data = file.read()
print(data)
file.close()

file = open('D:/Python Study/DS---1501/Self Study/Files/encripted_text.txt', 'r')
data = file.read()
print(data)
file.close()
