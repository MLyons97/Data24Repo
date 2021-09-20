# Gets the initial word which will attempt to be guessed
def get_initial_word() -> str:
    parser = True                                                        # A 'parser' variable here used with the while loop to ensure
    while parser:                                                        # that all inputs are only alphabetical
        key = input("Please enter the word you want them to guess: ")    # Gets input
        if key.isalpha():                                                # Checks for alphabetical answer
            return key.lower()                                           # Returns the word if good
        else:                                                            # Loops again if not
            print("Try again, make sure it is only one word and it only contains letters")


# Takes the inputted word, and generates the clue that will be used to guess
def generate_key(string: str) -> str:                                    # Takes the accepted initial word
    guess_string = ""
    for i in range(len(string)):                                         # and fills an empty string with underscores
        guess_string += "_"                                              # to match the answer key
    return guess_string


# Draws the output based on the number of incorrect guesses
def draw_picture(incorrect_guesses: int):
    for i in range(incorrect_guesses):                                   # Loops up to the number of wrong guesses
        print(list_of_drawings[i])                                       # Prints lines from an array to build image
    print("\n")
    return 0                                                             # Completeness


# Array holding each row of hanging man - not a function but very global
list_of_drawings = ['  _________'
, '  |       |'
, ' ( )      |'
, '  |       |'
, ' /|\      |'
, '  |       |'
, ' / \      |'
, '/   \     |      <-- Dead']


# Obtains and error checks the guess
def get_input(guessed_letters: str) -> str:                                     # Will output the guess as a length 1 string, takes the previously guessed letters
    error = True                                                                # Error boolean and the below while loop
    while error:                                                                # to ensure correct format
        guess = input("Please enter one letter to guess - ")                    # Obtains initial input
        if len(guess) > 1 or not guess.isalpha():                               # Frst pass is if it is a) one digit
            print("Try again, make sure it's only one letter")                  # and b) a letter
        elif guess in guessed_letters:                                          # Second pass checks for previously
            print(f"Try again, you have already guessed {guessed_letters}")     # guessed letter
        else:
            return guess.lower()                                                # If both of these checks are passed, returns the guess (in lower case)


# Logs the guess for future reference
def log_input(guessed_letters: str, guess: str) -> str:                         # Appends guess onto list of past
    return guessed_letters + guess                                              # guesses


# Is the guess in the word?
def is_letter_in_the_word(guess: str, answer: str) -> bool:                     # Simple function to "clean" letters and return
    return guess.lower() in answer.lower()                                      # boolean based on if it is correct or not


# What to do if the guess is correct
def letter_is_right(answer: str, guess: str, underscores: str, wcount: int) -> str:     # Actions to take if the previous is true
    print('Correct.')                                                           # Takes correct answer, the guess, the current state of the game and the count of wrong guesses
    draw_picture(wcount)
    where_is_the_character = []                                                 # List is needed if there are multiple instances of the letter
    for position, character in enumerate(answer):
        if character == guess:                                                  # Picks out instances of the correct guess
            where_is_the_character.append(position)                             # And adds them to the list
    for i in where_is_the_character:                                            # Loops over the list and
        underscores = underscores[:i] + guess + underscores[i + 1:]             # replaces the underscore in the current SoG with the correct letter
    print(f"The clue is now {underscores}\n")                                   # Prints the current state of game and
    return underscores                                                          # returns it for future use


# What to do if letter is incorrect
def letter_is_wrong(guess: str, wcount: int) -> int:
    print(f'Wrong - {guess} is not in the word.')                   # Prints a message to let the player know
    wcount += 1                                                     # Increases the 'wrong' counter
    draw_picture(wcount)                                            # Draws the updated hangman
    return wcount                                                   # Returns the 'wrong' counter for later use


# Formats and prints the past guesses
def show_past_guesses(guess_string):
    guess_list = []                                                 # First puts the guesses into a list (to format)
    for i in range(len(guess_string)):
        guess_list.append(guess_string[i])
    print(f"So far you have guessed: {', '.join(guess_list)}")      # And then prints a statement with them all back
    return 0                                                        # in a new string but with spaces and commas


# Gives the completeness of the game as a boolean
def final_check(answer: str, guess: str, lives: int) -> bool:
    if answer != guess:                                             # Also prints a message if the game is not over
        print(f"After that round you have {lives} lives left.\n")
        return False
    else:
        return True


# Runs the game
def run():
    answer_str = get_initial_word()                                     # Gets the answer
    guess_str = generate_key(answer_str)                                # and feeds it to generate the key
    incorrect_guesses_no = 0                                            # Initialising counter variables
    past_guesses_vals = ""
    no_of_lives = 8                                                     # Keep this at 8 for drawing

    while incorrect_guesses_no < no_of_lives:                           # Failsafe loop - the game will end after 8 mistakes
        show_past_guesses(past_guesses_vals)                            # Print previous guesses
        this_guess = get_input(past_guesses_vals)                       # Gets current guess and
        past_guesses_vals = log_input(past_guesses_vals, this_guess)    # updates the list of letters guessed

        if is_letter_in_the_word(this_guess, answer_str):               # Gets a boolean of if the guess is correct
            guess_str = letter_is_right(answer_str, this_guess, guess_str, incorrect_guesses_no)
        else:
            incorrect_guesses_no = letter_is_wrong(this_guess, incorrect_guesses_no)

        if final_check(answer_str, guess_str, 8-incorrect_guesses_no):  # A check to see if the answer has been reached
            break                                                       # and if it has, breaks out of the loop to the close
    if incorrect_guesses_no == no_of_lives:                             # If the maximum number of guesses is reached when
        print("You have killed a man on this day.\nLook at him :(")     # the game over is reached, then the full hangman
        draw_picture(8)                                                 # is shown, along with a sad message
    else:
        print("Congratulations! Man has not hanged :)")                 # If the word is guessed, the player is rewarded
                                                                    # with a congratulation and a smile
