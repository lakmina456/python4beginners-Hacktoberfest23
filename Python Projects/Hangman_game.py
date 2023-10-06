import random

def choose_random_word():
    word_list = ["python", "hangman", "programming", "challenge", "example"]
    return random.choice(word_list)

def play_hangman():
    word = choose_random_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(f"Word: {display_word}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            if set(guessed_letters) == set(word):
                print("Congratulations! You've guessed the word: " + word)
                break
        else:
            print("Incorrect guess!")
            attempts -= 1

    if attempts == 0:
        print("You've run out of attempts. The word was: " + word)

if __name__ == "__main__":
    play_hangman()
