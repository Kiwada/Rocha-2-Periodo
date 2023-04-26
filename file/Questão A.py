lista = []
file = open("file.in" , "r")
for linha in file:
        somatorio = cont = 0
        linha = linha.strip()
        print(linha)
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
    


