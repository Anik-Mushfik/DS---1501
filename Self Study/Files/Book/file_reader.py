file = open("pi_digits.txt", "r")
data = file.read()
data = data.rstrip('\n')
print(data)
file.close()