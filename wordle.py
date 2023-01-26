# IMPORT ALL THE REQUIRED PACKAGES
import random
from termcolor import colored

# DECLARE SOME VARIABLES
chances = 0
max_chances = 5
true_check = 0

true_check = False

# LIST OF ALL THE WORDS
words = [
    "input",
    "words",
    "ahmed",
    "games"
]

# CHOOSE A RANDOM WORD FROM WORDS AND SPLIT IT INTO A LIST
random_word = random.choice(words)
splitted_random_word = ([*random_word])

# PRINT THE TITLE 
print("\n******WORDLE******\n")

# LOOP UNTIL CHANCES IS SMALLER THAN MAX_CHANCES AND TRUE_CHECK IS FALSE
while chances < max_chances and not true_check:
    # TAKE THE USER INPUT AND SPLIT IT INTO A LIST
    user_input = input("Guess: ")
    splitted_input = ([*user_input])

    # DECLARE A VARIABLE FOR RIGHT WORD COUNTER
    true_check_counter = 0

    # GIVE AN ERROR IF SPLITTED_INPUT'S LENGTH IS SMALLER THAN OR GREATER THEN 5
    if len(splitted_input) > 5 or len(splitted_input) < 5:
        print("Enter a word with only 5 letters")
    # IF NOT RUN THIS
    else:
        # LOOP THROUGH THE LENGTH OF SPLITTED_INPUT
        for i in range(len(splitted_input)):
            # IF THE LETTER IS NOT THE LAST LETTER IN THE WORD
            if i != len(splitted_input) - 1:
                # IF THE VALUES AT THE SAME INDEX OF SPLITTED_INPUT AND SPLITTED_RANDOM_WORD ARE EQUAL
                if splitted_input[i] == splitted_random_word[i]:
                    # PRINT THAT LETTER IN GREEN COLOR AND INCREMENT THE TRUE CHECK COUNTER
                    print(colored(splitted_input[i], 'green'), end=" ")
                    true_check_counter += 1
                # ELSE IF THE VALUE OF SPLITTED_INPUT AT THAT PARTICULAR INDEX IS IN SPLITTED_RANDOM_NUMBER
                elif splitted_input[i] in splitted_random_word:
                    # PRINT THAT LETTER IN YELLOW COLOR
                    print(colored(splitted_input[i], 'yellow'), end=" ")
                # IF NOTHING OF THE ABOVE IS TRUE
                else:
                    # PRINT THAT LETTER IN THE DEFAULT COLOR (WHITE)
                    print(colored(splitted_input[i]), end=" ")
            # IF THE LETTER NOT THE LAST LETTER IN THE WORD, JUST MOVE TO A NEW LINE (REMOVE end=" ")
            else:
                if splitted_input[i] == splitted_random_word[i]:
                    print(colored(splitted_input[i], 'green'))
                elif splitted_input[i] in splitted_random_word:
                    print(colored(splitted_input[i], 'yellow'))
                else:
                    print(colored(splitted_input[i]))
        # IF TRUE_CHECK_COUNTER IS LESS THAN 4 (THAT MEANS ALL THE VALUES OF THE 2 LISTS ARE NOT EQUAL)
        if true_check_counter < 4:
            # DO NOTHING
            pass
        # IF THEY ARE EQUAL
        else:
            # MAKE TRUE_CHECK TO TRUE AND THE LOOP WILL ABORT
            true_check = True
                
    chances += 1

# IF THE TRUE CHECK IS TRUE
if true_check:
    # PRINT THE WINNING TEXT
    print("You guessed it correct!")
# IF IT IS NOT TRUE
else:
    # PRINT THE LOOSING TEXT
    print("You couldn't guess the word! It was", random_word)
