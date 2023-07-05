# Imports PIL module  
import random

import PIL
from PIL import Image

import sys
# open method used to open different extension image file
wordlist=['aquafina','bridgestone','goodyear','michelin','nestle',
          'royaldutchshell','sonyericsson','texasinstruments','tommyhilfiger',
          'olay','rivian','schand','tesla','uber','unilever']

secretword= random.choice(wordlist)
length_word = len(secretword)
alphabet = "abcdefghijklmnopqrstuvwxyz"
guess_word = []
letter_storage=[]



def newFunc():

    while True:
        gameChoice = input("Would You like to play hangman?\n").upper()

        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("come back next time")
        else:
            print("Please Answer only Yes or No")
            continue

newFunc()



def change():

    for character in secretword: # printing blanks for each letter in secret word
        guess_word.append("-")

    print("Ok, so the word You need to guess has", length_word, "characters")

    print("Be aware that You can enter only 1 letter from a-z\n\n")

    print(guess_word)



#shows pics
if(secretword=='aquafina'):
      im = Image.open(r"hangman pics/aquafina logo.png")
      im.show()

if(secretword=='bridgestone'):
      im = Image.open(r"hangman pics/bridgestone logo.png")
      im.show()

if(secretword=='goodyear'):
      im = Image.open(r"hangman pics/goodyear logo.png")
      im.show()

if(secretword=='michelin'):
      im = Image.open(r"hangman pics/michelin logo.png")
      im.show()

if(secretword=='nestle'):
      im = Image.open(r"hangman pics/nestle logo.png")
      im.show()

if(secretword=='royaldutchshell'):
      im = Image.open(r"hangman pics/Royal Dutch Shell logo.jpg")
      im.show()

if(secretword=='sonyericsson'):
      im = Image.open(r"hangman pics/sony logo.png")
      im.show()

if(secretword=='texasinstruments'):
      im = Image.open(r"hangman pics/texas instr logo.png")
      im.show()

if(secretword=='tommyhilfiger'):
      im = Image.open(r"hangman pics/tommy hilfiger logo.jpg")
      im.show()

if(secretword=='olay'):
      im = Image.open(r"new pictures/olay logo.jpg")
      im.show()

if(secretword=='rivian'):
      im = Image.open(r"new pictures/rivian logo.jpg")
      im.show()

if(secretword=='schand'):
      im = Image.open(r"new pictures/schand logo.png")
      im.show()

if(secretword=='tesla'):
      im = Image.open(r"new pictures/tesla logo.jpg")
      im.show()

if(secretword=='uber'):
      im = Image.open(r"new pictures/uber logo.png")
      im.show()

if(secretword=='unilever'):
      im = Image.open(r"new pictures/unilever logo.jpg")
      im.show()




def guessing():
    guess_taken = 1
    while guess_taken < 7:


        guess = input("Pick a letter\n").lower()

        if not guess in alphabet: #checking input
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage: #checking if letter has been already used
            print("You have already guessed that letter!")
        else: 

            letter_storage.append(guess)
            if guess in secretword:
                print("You guessed correctly!")
                for x in range(0, length_word): #This Part I just don't get it
                    if secretword[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won!")
                    break
            else:
                if (guess_taken == 1):
                                    print ("_________")
                                    print ("|	 |")
                                    print ("|	 O")
                                    print ("|")
                                    print ("|")
                                    print ("|")
                                    print ("|________")
                print("The letter is not in the word. Try Again!")
                if (guess_taken == 2):
                                    print ("_________")
                                    print ("|	 |")
                                    print ("|	 O")
                                    print ("|	 |")
                                    print ("|	 |")
                                    print ("|")
                                    print ("|________")
                elif (guess_taken == 3):
                                    print ("_________")
                                    print ("|	 |")
                                    print ("|	 O")
                                    print ("|	\|")
                                    print ("|	 |")
                                    print ("|")
                                    print ("|________")
                elif (guess_taken == 4):
                                    print ("_________")
                                    print ("|	 |")
                                    print ("|	 O")
                                    print ("|	\|/")
                                    print ("|	 |")
                                    print ("|")
                                    print ("|________")
                elif (guess_taken == 5):
                                    print ("_________")
                                    print ("|	 |")
                                    print ("|	 O")
                                    print ("|	\|/")
                                    print ("|	 |")
                                    print ("|	/ ")
                                    print ("|________")
                elif (guess_taken == 6):
                                    print ("_________")
                                    print ("|	 |")
                                    print ("|	 O")
                                    print ("|	\|/")
                                    print ("|	 |")
                                    print ("|	/ \ ")
                                    print ("|________")
                                    print ("\n")
                if guess_taken == 6:
                        print("Sorry, You lost :<! The word was",         '"',secretword,'"')
                guess_taken +=1


change()
guessing()

if(secretword=='aquafina'):
      im = Image.open(r"hangman pics/aquafina image.jpg")
      im.show()

if(secretword=='bridgestone'):
      im = Image.open(r"hangman pics/bridgestone image.png")
      im.show()

if(secretword=='goodyear'):
      im = Image.open(r"hangman pics/goodyear image.png")
      im.show()

if(secretword=='michelin'):
      im = Image.open(r"hangman pics/michelin image.jpg")
      im.show()

if(secretword=='nestle'):
      im = Image.open(r"hangman pics/nestle image.jpg")
      im.show()

if(secretword=='royaldutchshell'):
      im = Image.open(r"hangman pics/Royal dutch shell image.png")
      im.show()

if(secretword=='sonyericsson'):
      im = Image.open(r"hangman pics/sony image.png")
      im.show()

if(secretword=='texasinstruments'):
      im = Image.open(r"hangman pics/texas instr image.png")
      im.show()

if(secretword=='tommyhilfiger'):
      im = Image.open(r"hangman pics/tommy hilfiger image.png")
      im.show()

if(secretword=='olay'):
      im = Image.open(r"new pictures/olay image.png")
      im.show()

if(secretword=='rivian'):
      im = Image.open(r"new pictures/rivian image.jpg")
      im.show()

if(secretword=='schand'):
      im = Image.open(r"new pictures/schand image.png")
      im.show()

if(secretword=='tesla'):
      im = Image.open(r"new pictures/tesla image.jpg")
      im.show()

if(secretword=='uber'):
      im = Image.open(r"new pictures/uber-to be cropped.jpg")
      im.show()

if(secretword=='unilever'):
      im = Image.open(r"new pictures/unilever image.png")
      im.show()



print("Game Over!")
