def converter(arq_ini , arq_dest):
    file_ini = open(arq_ini , "r")
    file_dest= open(arq_dest , "w")
    for linha in file_ini:
        for letra in linha:
           file_dest.write(letra.upper())
    




def principal():
    arq_ini = input("Arquivo de origem .:")
    arq_dest = input("Arquivo de destino:")
    converter(arq_ini , arq_dest)