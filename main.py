
import random

from hangman_words import word_list
from hangman_art import stages,logo

#word_list = ["camel", "baboon", "patriarchy"]

chosen_word = random.choice(word_list)

display = []

word_length = len(chosen_word)

end_of_game = False

lives = 6

print(logo)

#print(f'!!! The solution is {chosen_word}.\n')


for _ in range(word_length):
  display += '_'


while not end_of_game:
  guess = input("Guess a letter : ").lower()
  
  for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
      display[position] = letter
     
  if guess not in chosen_word:
    print(f"\nYou guessed {guess}, that's not in the word. You loss a life.")
    lives -= 1
    print(f"\nLife remains : {lives}")
    if lives == 0:
      end_of_game = True
      print("\nYou lose")
    
  
  print("\n")
  print(display)
  
  if '_' not in display:
    end_of_game = True
    print("\nYou win")
    
  print(stages[lives])
  
  
  
