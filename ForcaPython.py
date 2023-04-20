palavra_secreta = ["M" , "A" , "C" ,"I","O"]  #Palavra a ser descoberta
letras_descobertas = []


print("\n*** Jogo da Forca *** \n")


for i in range(0 , len(palavra_secreta)): #loop para que as letras descobertas
    letras_descobertas.append("-")        #para cada letra na palavra secreta vou 
                                          #adicionar um traço para o usuario.


acertou = False                          #comando boleano para acertou ser false     




while acertou == False:                #enquanto acertou for falso
    letra = str(input("Digite a Letra : ")) #usuario digita uma letra para 
                                            #adivinhar a letra da forca
    
    
    for i in range(0 , len(palavra_secreta)):  #percorrer a palavra secreta para verificar se a letra  esta dentro da palavra secreta

        if letra == palavra_secreta[i] :       #se a letra estiver na posição I da palavra secreta
         letras_descobertas[i] = letra         #palavra secreta com os traços vai receber a letra digitada
            
        print(letras_descobertas[i])     # imprimir a letra no traço correspondente



    acertou = True
    

    for x in range(0,len(letras_descobertas)): #verifica se ainda traços na palavra
         if letras_descobertas[x] == "-" :
          acertou = False






if letras_descobertas == palavra_secreta:
  print('Parabéns Desafio Concluido :D ')
         
    


 



    
   