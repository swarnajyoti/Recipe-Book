# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 00:30:59 2019

@author: Swarnajyoti
"""

import sys

f = open('recipebook.txt', 'w')

def recipe():
    title = input("Great! So, What is your recipe? ")
    ingredients = input("Ingredients? ")
    step1 = input("What do we do first in order to prepare the dish? ")
    step2 = input("Next? ")
    step3 = input("And after that? ")
    step4 = input("How do we know when the reciple is finished? ")
    step5 = input("What is the best way of garnishing your dish? ")

    print(title + '\n', ingredients + '\n', step1 + '\n', step2 + '\n', step3 + '\n', step4 + '\n', step5 + 'n', file = f)
    


print("Welcome to your Recipe Book. What would you like to try? ")
answer = input()

if answer == "yes":
  recipe()
else:
    print("Being Lazy? Okay, next time might be. Thanks for visiting.")