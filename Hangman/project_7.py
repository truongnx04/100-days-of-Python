import random

from hangman_word_list import word_list 
import hangman_art


lives = 6

print(hangman_art.LOGO)
chosen_word = random.choice(word_list)
# print(chosen_word) - ĐÁP ÁN

placeholder = ""
word_length = len(chosen_word) 
for position in range(word_length):
    placeholder += "_"
print(placeholder)    

game_over = False
correct_letter = []

while not game_over:

    print(f"**********{lives}/6 LIVES LEFT**********")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letter:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter    
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess} , that's not in the word. You lose a life. ")
            if lives == 0:
                print("**********YOU LOSE**********")
                print(f"It's was {chosen_word}")
                game_over = True
                

    if "_" not in display:
        print("**********YOU WIN**********")
        game_over = True

    print(hangman_art.HANGMANPICS[6 - lives]) #Hình từ 0 - 6     

                                