#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange



player1 = [50, 3]
player2 = [50, 0]
while True:
    user_choice = ""
    while user_choice not in ["1", "2"]:
        user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")
    
    # mode attaque
    if user_choice == "1":
        a = randrange(5, 11)
        b = randrange(0, 16)
        player1[0] -= b
        player2[0] -= a
        print(f"santé du player1 : {player1[0]}")
        print(f"santé du player2 : {player2[0]}")
        
    # mode potion 
    if user_choice =="2" and int(player1[1]) > 0:
        potion = randrange(15, 51)
        player1[0] += potion
        player1[1] -= 1
        print(f"Bonus santé {player1[0]}")
        # les 2 attaques de l'ennemi
        print("Première attaque de l'adversaire")
        b = randrange(0, 16)
        player1[0] -= b
        print(f"santé du player1 : {player1[0]}")
        print(f"santé du player2 : {player2[0]}")
        print("Deuxième attaque de l'adversaire")
        b = randrange(0, 16)
        player1[0] -= b
        print(f"santé du player1 : {player1[0]}")
        print(f"santé du player2 : {player2[0]}")
    elif int(player1[1]) == 0:
        print("Player1 tu n'a plus de potion")
    
    if player1[0] <= 0 and player2[0] > player1[0]:
        print("player1 tu as perdu tu n'as plus de point de vie")
        break
    elif player2[0] <=0 and player1[0] > player2[0]:
        print("player2 tu as perdu tu n'as plus de point de vie")
        break
        
print("Fin du jeu.")