file = open("pi_digits.txt", "r")
data = file.read()
data = data.rstrip('\n')
print(data)
file.close()

file = open('D:\Python Study\DS---1501\Self Study\Files\Book\pi_digits.txt', 'r')
data = file.readlines()
print(data)

cont = ""
for line in data:
    print(line.strip(), end="")
print()

for l in data:
    cont += l.strip()

print(cont)
print(len(cont))
file.close()


file = open("D:\Python Study\DS---1501\Self Study\Files\Book\hello.txt", "r")
data = file.readlines()
file.close()

file = open("D:\Python Study\DS---1501\Self Study\Files\Book/new.txt", "w")
for lie in data:
    file.write(lie)
file.close()