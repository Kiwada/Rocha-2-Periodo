arquivo = open('dados_pessoas1.txt', 'a')

while True:
    nome = input('Digite o nome da pessoa (ou "fim" para encerrar): ')
    if nome == 'fim':
        break
    telefone = input('Digite o telefone da pessoa: ')
    nascimento = input('dd/mm/aaaa: ')

   
    arquivo.write(nome + ';' + telefone + ';' + nascimento + '\n')


arquivo.close()


arquivo = open('dados_pessoas1.txt', 'r')


for linha in arquivo:
  
    campos = linha.strip().split(';')

  
    print('Nome: ' + campos[0])
    print('Fone: ' + campos[1])
    print('Nasc: ' + campos[2])
    print('===============')


arquivo.close()