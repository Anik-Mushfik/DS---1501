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