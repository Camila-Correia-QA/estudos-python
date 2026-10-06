'''Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer
 qual deles é maior
'''
import math

def maior(*núm):
    v = max(*núm)
    l = len(núm)
    print(f'Foram informados {l} números ao todo')
    print(f'O maior número é {v}')

maior(5,4,8,7,8,9,8,1,100)
