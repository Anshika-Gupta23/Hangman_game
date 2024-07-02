#from replit import clear
import random
import hangman_art as h_a
import hangman_words as h_w

word_list = h_w.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(h_a.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed the letter \"{guess}\" ")
    #Check guessed letter
    else:
        for position in range(word_length):
            letter = chosen_word[position]  
           #if guessed letter is right
            if letter == guess:
                print("You have guessed the right letter\n")
                display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"The letter \"{guess}\" is not present in the word. You lost a life ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost the game. :(")
        print(lives)
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win. :)")

    print(h_a.stages[lives])
