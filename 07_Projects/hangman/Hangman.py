from Visuals import hangman_visual
from random import choice


rdm_word = choice(["python", "restaurant", "church", "apple", "university", "barbecue", "keyboard", "sage"])        # choose a rdm word from list
letters_in_word = set(rdm_word)                                                                                     # set word as a new iterable
guessed_letters = []                                                                                                # list where letters are stored later

def print_letters():                                                                                                # function to print letters
    for letter in rdm_word:                                                                                         # for every letter in rdm_word
        if letter in guessed_letters:                                                                               # if the letter is in it
            print(f"{letter}", end=" ")                                                                             # print the letter
        else:                                                                                                       # if not, print an underscore
            print("_", end=" ")  
    print()  

def print_visuals(mistake_count):                                                                                   # function to print the current hangman visual
    for mistake in hangman_visual[mistake_count]:                                                                   # key: mistake_count value: ascii gfx
        print(mistake)
        

def main():                                                                                                         # main
    is_playing = True                                                                                               
    mistake_count = 0                                                                                               

    print("Welcome to the Hangman Game!")
    
    while is_playing:
        print_visuals(mistake_count)                                                                                # print visuals
        print_letters()                                                                                             # print letters or underscores
        
        if mistake_count >= len(hangman_visual) - 1:                                                                # loose condition
            print(f"\nBig ouch! You lost.\nThe word was: {rdm_word}.")
            is_playing = False                                                                                      # end game
        elif set(guessed_letters) >= letters_in_word:                                                               # win condition
            print(f"\nCongrats! You won.\nThe word was: {rdm_word}.")                                           
            is_playing = False                                                                                      # end game
        else:                                                                                                       # in game
            guess = input("Guess a letter: ").lower()                                                               # ask user for letter
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'.")                 
            elif len(guess) != 1 or not guess.isalpha():                                                            # if more than 1 letter or not aplhabetical input
                print("Invalid input. Use only one letter.")
            else:
                guessed_letters.append(guess)                                                                       # add guess to guessed_letters
                if guess in letters_in_word:                                                                        # if its in the rdm word
                    print(f"'{guess}' is in the word.")                                                             # congrats
                else:                                                                                               # if not
                    print(f"Ouch. '{guess}' is not in the word.")                                                   # well. try harder next time
                    mistake_count += 1                                                                              # increment mistake_count

if __name__ == "__main__":
    main()
