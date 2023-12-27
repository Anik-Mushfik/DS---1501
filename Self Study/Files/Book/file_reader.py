file = open("pi_digits.txt", "r")
data = file.read()
data = data.rstrip('\n')
print(data)
file.close()

file = open('D:\Python Study\DS---1501\Self Study\Files\Book\pi_digits.txt', 'r')
data = file.readlines()
print(data)

for line in data:
    print(line.strip(), end="")