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