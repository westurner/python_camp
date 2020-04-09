#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:27:04 2020

@author: Kirby Swallows Sans
"""
import random

class Animal:
    pass

class Mammal(Animal):

    def __init__(self, nm, how_old):
        self.name = nm
        self.age = how_old
        self.stomach = [ ]

    def eat(self, food):
        self.stomach.append(food)
        
    def barf(self):
        contents = " ".join(self.stomach)
        self.stomach = [ ]
        return contents
                
class Cat(Mammal):

    def meow(self, n=1):
        return "meow!" * n
    
    def __repr__(self):
        return 'Cat("{}", {})'.format(self.name, self.age)
    
class Dog(Mammal):
        
    def bark(self, n=1):
        return "bark!" * n
    
    def __repr__(self):
        return 'Dog("{}", {})'.format(self.name, self.age)
    
def test_dog():
    doggie = Dog("Rover", 3)
    foods = """
    🍄 🍅 🍆 🍇 🍈 🍉 🍊 🍌 🍍 🍎 
    🍏 🍐 🍑 🍒 🍓 🍔 🍕 🍗 🍘 🍙 
    🍚 🍛 🍜 🍝 🍞 🍟 🍠 🍢 🍣 🍤 
    🍥 🍦 🍧 🍨 🍩 🍪 🍫 🍭 🍮 🍯 
    🍰 
    """.split()
    # eat between one and five things
    meal = random.choices(foods, k=random.randint(1, 5))
    print("Eating a meal of {} things".format(len(meal)))
    for f in meal:
        doggie.eat(f)
    # oh oh, something doggie ate was unsuitable
    print("doggie doesn't feel well.")
    print(doggie.barf())
    
def test_cat():
    cat = Cat("Felix", 2)
    foods = """
    🍄 🍅 🍆 🍇 🍈 🍉 🍊 🍌 🍍 🍎 
    🍏 🍐 🍑 🍒 🍓 🍔 🍕 🍗 🍘 🍙 
    🍚 🍛 🍜 🍝 🍞 🍟 🍠 🍢 🍣 🍤 
    🍥 🍦 🍧 🍨 🍩 🍪 🍫 🍭 🍮 🍯 
    🍰 
    """.split()
    # eat between one and five things
    meal = random.choices(foods, k=random.randint(1, 5))
    print("Eating a meal of {} things".format(len(meal)))
    for f in meal:
        cat.eat(f)
    # oh oh, something doggie ate was unsuitable
    print("doggie doesn't feel well.")
    print(cat.barf())
    
    
if __name__ == "__main__":
    test_dog()
    test_cat()
    
    