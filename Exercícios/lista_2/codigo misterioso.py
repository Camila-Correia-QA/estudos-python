''' Olá, jovem programadora! Temos um desafio divertido para você hoje.
Vamos criar um programa que codifica mensagens secretas usando algo chamado ROT13.
Não se preocupe se parecer complicado no início - vamos explicar tudo passo a passo.
ROT13 é como uma linguagem secreta. Imagine que você quer escrever uma mensagem
que só sua melhor amiga possa ler. O ROT13 ajuda nisso! Ele pega cada letra da sua
mensagem e a substitui por outra letra que está 13 posições à frente no alfabeto.
Por exemplo, a letra 'A' se tornaria 'N', 'B' viraria 'O', e assim por diante.
Quando chega no 'Z', volta para o início do alfabeto. Então 'Z' vira 'M'. Legal, né?
É como um código secreto super fácil de usar!
Seu desafio é criar um programa em Python que faça isso. Não se preocupe se você não
souber tudo sobre Python ainda. Vamos te dar algumas dicas para começar. O objetivo é
que você digite uma mensagem e o programa mostre como ela ficaria codificada em ROT13.
 Algumas coisas para pensar: Como você pode pegar cada letra da mensagem? Como saber
 qual letra vem 13 posições depois no alfabeto? O que fazer com espaços e pontuação?
 Lembre-se, programar é como resolver um quebra-cabeça. Divirta-se tentando! C'''

def  krypton (string,offset):
    krypt = ''
    for c in string:
        if (c >= 'a' and c <= 'z'):
            aux = ord(c)+offset-ord('a')
            krypt += chr(ord('a')+aux%26)
        elif (c >= 'A' and c <= 'Z'):
            aux = ord(c) + offset - ord('A')
            krypt += chr(ord('A') + aux % 26)
        else:
            krypt += c
    return krypt

menssager = input('Digite sua mensagem: ')
offset = int(input('Digite um número: '))
pergunta = input('Deseja criptografar ou descriptografar?c/d').upper()
if pergunta == 'D':
    menssager_kryptografada = krypton(menssager,-offset)
else:
    menssager_kryptografada = krypton(menssager,offset)
print(f'O código é {menssager_kryptografada}')
