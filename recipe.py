# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 00:30:59 2019

@author: Swarnajyoti
"""

import sys

f = open('recipe.txt', 'w')

def recipe():
    title = input("Great! What would you like to call your recipe? ")
    ingredients = input("What ingredients are in your recipe? ")
    step1 = input("What do we do first in order to prepare the dish? ")
    step2 = input("What comes next? ")
    step3 = input("And after that? ")
    step4 = input("How do we know when the reciple is finished? ")
    step5 = input("What is the best way to serve the dish? ")

    print(title + '\n', ingredients + '\n', step1 + '\n', step2 + '\n', step3 + '\n', step4 + '\n', step5 + 'n', file = f)
    


print("Welcome to recipe maker. Would you like to start a new recipe? ")
answer = input()

if answer == "yes":
  recipe()
else:
    print("That's too bad, maybe next time. Thanks for visiting.")