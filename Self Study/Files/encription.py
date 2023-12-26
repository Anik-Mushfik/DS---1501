def cipher_enco(text):
    new = ''
    for i in text:
        asci = ord(i)
        if (65<=asci and asci<90) or (97<asci and asci<122):
            i = chr(asci+1)
        elif asci == 90:
            i = 'A'
        elif asci == 122:
            i = 'a'
        new += i
    
    return new

file = open("D:/Python Study/DS---1501/Self Study/Files/message.txt", "r")
data = file.read()
new_text = cipher_enco(data)
print(new_text)
file.close()
  
file = open("D:/Python Study/DS---1501/Self Study/Files/encripted_text.txt","w")
file.write(new_text)
file.close()
