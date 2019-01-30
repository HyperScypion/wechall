def decrypt(string, key:int):   
    decrypted = ""
    chars = []
    for char in string:
        pom = ord(char) - key
        if pom < 65:
            pom += 62
        decrypted += chr(pom)
    print(decrypted)

decrypt('PDA MQEYG XNKSJ BKT FQILO KRAN PDA HWVU ZKC KB YWAOWN WJZ UKQN QJEMQA OKHQPEKJ EO JANBWJJWIDCL', 1)
