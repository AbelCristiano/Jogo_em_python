import random

def rodar_jogo(jogada):
    #Jogada 1 == pedra
    #Jogada 2 == papel
    #Jogada 3 == tesoura
    
    escolha = random.randint(1, 3)
    
    print(escolha)
    print(jogada)
    
    if jogada == escolha: 
        print('Empate')
        return 3
    else: 
        #jogada == pedra
        if jogada == 1:
            if escolha == 2:
                print('Você jogou pedra e perdeu!')
                return 2
            elif escolha == 3:
                print('Você jogou pedra e ganhou!')
                return 1
             
        #jogada == papel        
        elif jogada == 2:
            if escolha == 1:
                print('Você jogou papel e perdeu!')
                return 2
            elif escolha == 3:
                print('Você jogou papel e ganhou!')
                return 1
            
        #jogada == tesoura        
        elif jogada == 3:
            if escolha == 1:
                print('Você jogou tesoura e perdeu!')
                return 2
            elif escolha == 2:
                print('Você jogou tesoura e ganhou!')
                return 1
                