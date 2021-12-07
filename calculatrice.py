#!/usr/bin/env python3
# -*- coding: utf-8 -*-

nombre = ('premier', 'deuxième')
nbre = []
for i in range(2):
    phrase = "Entrez un " + nombre[i] +" nombre : "
    val = input(phrase)
    while not val.isdigit():
        print("Veuillez entrer un nombre valide")
        val = input(phrase)
    nbre.insert(i,val)
print(f"Le résultat de l'addition de {nbre[0]} avec {nbre[1]} est égal à {int(nbre[0]) + int(nbre[1])}")
