import random

WORDS = ["python", "developer", "computer", "programming", "keyboard"]
MAX_WRONG_GUESSES = 6

def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = set()

    print("=== Hangman Game ===")
    print(f"Guess the word. You have {MAX_WRONG_GUESSES} incorrect guesses.")

    while len(wrong) < MAX_WRONG_GUESSES:
        display = " ".join(letter if letter in guessed else "_" for letter in word)
        print(f"\nWord: {display}")
        print(f"Wrong guesses ({len(wrong)}/{MAX_WRONG_GUESSES}): {', '.join(sorted(wrong)) or 'None'}")

        if all(letter in guessed for letter in word):
            print("You won! Great guessing.")
            return

        guess = input("Enter one letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue
        if guess in guessed or guess in wrong:
            print("You already tried that letter.")
            continue
        if guess in word:
            guessed.add(guess)
            print("Correct!")
        else:
            wrong.add(guess)
            print("Incorrect.")

    print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    play()
