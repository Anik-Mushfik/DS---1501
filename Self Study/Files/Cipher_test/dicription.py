def cipher_dico(text):
    new = ''
    for i in text:
        asci = ord(i)
        if (65<asci and asci<=90) or (97<asci and asci<=122):
            i = chr(asci-1)
        elif asci == 65:
            i = 'Z'
        elif asci == 97:
            i = 'z'
        new += i
    
    return new

file = open("D:/Python Study/DS---1501/Self Study/Files/encripted_text.txt", "r")
data = file.read()
new_text = cipher_dico(data)
print(new_text)
