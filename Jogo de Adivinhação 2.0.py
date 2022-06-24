from random import randint

print('\n\033[37;1mTente adivinhar qual número o computador irá gerar:\033[m\n')

computador = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('\033[33mQual é o seu palpite?\033[m '))
    palpites += 1

    if jogador == computador:
        acertou = True
    
    else:
        if jogador < computador:
            print('\033[34;1mMais\033[m... Tente novamente!')

        if jogador > computador:
            print('\033[31;1mMenos\033[m... Tente novamente!') 

print(f'\n\033[32mVocê acertou em \033[32;1m{palpites}\033[m \033[32mtentativas. Parabéns!\033[m\n')
