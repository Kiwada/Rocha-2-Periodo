lista = []
file = open("file.in" , "r")
somatorio = 0
cont = 0
for linha in file: 
        linha = linha.strip()
        for letra in linha:
            if letra == 'a':
             cont += 1
            elif cont > 1:
              somatorio += cont
              cont = 0
            elif cont == 1:
              cont = 0
        if cont > 1:
           somatorio += cont
        print(somatorio)
    


