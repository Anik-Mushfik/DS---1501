from enco import cipher_enco
from dicri import cipher_dico

file = open("F:\Study\Python\DS---1501\Self Study\Files\message.txt","r")
text = file.read()
print(text)
new_text = cipher_enco(text)
print(f"Encripted: {new_text}")
print(f"Dicription: {cipher_dico(new_text)}")
