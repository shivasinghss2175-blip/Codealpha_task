import random

words = ["python", "coding", "computer", "college", "program"]
word = random.choice(words)

guessed = []
attempts = 6

print("\n--- HANGMAN GAME ---")

while attempts > 0:
    display = ""

    for letter in word:
        display += letter if letter in guessed else "_"
        display += " "

    print("\nWord:", display)
    print("Attempts left:", attempts)

    if all(letter in guessed for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter one alphabet only!")
    elif guess in guessed:
        print("Already guessed!")
    else:
        guessed.append(guess)


        if guess not in word:
            attempts -= 1
            print("Wrong guess!")
        else:
            print("Correct guess!")

else:
    print("\nGame Over! The word was:", word)