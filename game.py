# Create your Game class logic in here.
from phrase import Phrase
import random



class Game:
    
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('Is the juice worth the squeeze'), Phrase('Green Lights'), Phrase('An Arm and a Leg'), Phrase('Dime a Dozen'), Phrase('Down to the Wire')]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
        
    def welcome(self):
        GREETING = "==========================\n Welcome to Phrase Hunter\n=========================="
        print(GREETING.upper())
        rules = print("\nRules: \n******Try and guesses the phrase! Select a letter on a time, if you can't solve it before your 5 guess up you lose. Good luck!.******\n\n")    
    
    def get_random_phrase(self):
        sel_phrase = random.choice(self.phrases)
        return sel_phrase
    
    def start(self):
        self.welcome()
        print(f'Number missed: {self.missed}')
        self.active_phrase.display(self.guesses)
        self.get_guess()
        self.user_guess = self.get_guess()
        print(self.user_guess)
        self.guesses.append(self.user_guess)
        
        
        
    def get_guess(self):
        self.guess = input('Please enter letter: ')
        return self.guess
        
    
        