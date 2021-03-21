from words import word_list
from colorama import Fore, Back, Style,init
import random


init()

def get_word():
    word = random.choice(word_list)
    return word.upper()

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def play(word):
   word_completion = "-" * len(word)
   guessed = False
   guessed_letters = []
   guessed_words = []
   tries = 6
   print("Let's play Hangman!")
   print(Fore.RED)
   print(display_hangman(tries))
   print(Style.RESET_ALL) 
   print("Word: ", word_completion)
   print()
   print(f"Number of tries left: {tries}")
   print("\n")
   while not guessed and tries > 0:
      guess = input("Please guess a word or a letter: ").upper()
      if len(guess) == 1 and guess.isalpha():
         if guess in guessed_letters:
               print(Fore.YELLOW+'Already guessed the letter', guess)
               print(Style.RESET_ALL)
         elif guess not in word:
               print(Fore.RED)
               print(guess, "is not in the word!")
               print(Style.RESET_ALL) 
               tries -= 1
               guessed_letters.append(guess)
         else:
               print(Fore.GREEN)
               print(f"Good job {guess} is the word")
               print(Style.RESET_ALL)
               guessed_letters.append(guess)
               word_as_list = list(word_completion)
               indices = [i for i, letter in enumerate(
                  word) if letter == guess]
               for i in indices:
                  word_as_list[i] = guess
               word_completion = "".join(word_as_list)
               if "-" not in word_completion:
                  guessed = True

      elif len(guess) == len(word) and guess.isalnum():
         if guess in guessed_words:
               print(Fore.YELLOW+"You already guessed the word", guess)
               print(Style.RESET_ALL) 
         elif guess != word:
               print(Fore.RED)
               print(guess, "is not the word")
               print(Style.RESET_ALL)
               tries -= 1
               guessed_words.append(guess)
         else:
               guessed = True
               word_completion = word

      else:
         print("not a valied guess!")
      print(display_hangman(tries))
      print(word_completion)
      print("\n")
   if guessed:
      print("Congrats you guessed the word, you WIN!")
   else:
      print(Fore.RED+f"Sorry you ran out of tries {word}. May be Next time")
      print(Style.RESET_ALL)

def option():
   print(
      """
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
"""
)
   print("1. Play game \n2. How to play \n3. Credits \n4. Exit")
   ops = int(input("Enter the option number: "))
   if ops == 1:
      main()
   elif ops == 2:
      print("""
      Hangman is a paper and pencil guessing game for two or more players.
      One player thinks of a word, phrase or sentence and the other(s) tries to guess it by
      suggesting letters within a certain number of guesses.
      """)
      input("press any key: ")
      option()
   elif ops == 3:
      print("credits")
      print("""

      Developed by:
      1.Abhineet Saha
      2.Antar Mukhopadhyaya
      3.Shiladitya Das

      in guidance of Govind Prasad Arya
      """)
      input("press any key")
      option()
   elif ops==4:
      print("exit")
   else:
      print(Fore.RED+"Invalid Choice")
      print(Style.RESET_ALL)
      input("press any key")
      option()

def main():

   word = get_word()

   play(word)
   while input("play again? (Y/N): ").upper() == "Y":
      word = get_word()
      play(word)
   else:
      option()
if __name__ == "__main__":
   option()



