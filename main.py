from random import *
import os
import pyperclip

def gerador():
    os.system('cls' if os.name == 'nt' else 'clear')

    wMax = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    wMin = "abcdefghijklmnopqrstuvwxyz"
    num = "012345678901234567890123456789"
    cEsp = "!@#$&()!@#$&()"

    comp = cEsp + num + wMin + wMax

    quest = input('Quantos caracteres devem ter na senha? ')
    dig = int(quest)
    password = ""

    for i in range(dig):
        password += choice(comp)

    print(password)
    print('\nDesenha copiar a senha?\n\nS - Copiar\nG - Nova senha\n')

    quest1 = input('')

    if quest1 == "s" or quest1 == "S":
        pyperclip.copy(password)
    elif quest1 == "g" or quest1 == "G":
        gerador()

gerador()