file = open ('dados' , 'r')
for linha in file:
    linha = linha.strip()
    byte = linha.split()
    print (byte,end=" ")
    if len(byte) == 8 ==  (byte.count('0')) + byte.count('1'):
     if '9' in byte:
        print('f')
     else:
        print('s')