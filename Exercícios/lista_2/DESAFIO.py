'''Desafio: faça um Timer(Cronometro regressivo) Que hora minuto segundo
(Pode ler cada um separado), noo formato 0-23 h 0-59 m e 0-59 s Ele
tem que ir do horario lido de maneira regressiva ate 00:00:00.. POREM
nao pode usar if-else, e o for é apenas para imprimir a saida'''

from time import sleep


hora = 2

minuto = 2

segundo = 59

segundos_totais = (hora * 3600) + ( minuto * 60 ) + (segundo * 60)

print("\033c")

for tempo in range (segundos_totais):
    print(f'{hora:02}:{minuto:02}:{segundo:02}')
    sleep(1)
    segundo = segundo - 1
    if minuto == 0 and hora == 0 and segundo == 0:
        print(f'O tempo acabou 0{hora}:0{minuto}:0{segundo}')
        break
    if segundo < 0:
        segundo = 59
        minuto = minuto - 1
    if minuto < 0:
        minuto = 59
        hora = hora - 1
