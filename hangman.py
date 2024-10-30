import random

# List of possible words
words = ["python", "hangman", "challenge", "communication", "electronics", "instrumentation"]

def choose_word():
    # Randomly selects a word from the list
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with guessed letters and underscores for missing ones
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman_game():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Number of allowed wrong guesses

    print("Welcome to Hangman!")
    print("Guess the word letter by letter.")

    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        
        # Get user guess
        guess = input("Guess a letter: ").lower()

        # Check if guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        # Process the guess
        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
            # Check if all letters have been guessed
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print("Wrong guess.")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame Over! The word was: {word}")

# Start the game
hangman_game()
