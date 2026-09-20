import random

words = ["python", "ball", "college", "flower", "computer"]
word = random.choice(words)

guessed = ""
chances = 6

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display)
    print("Guessed letters:", guessed if guessed else "None")

    if "_" not in display:
        print("You Win!")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    guessed += guess

    if guess not in word:
        chances -= 1
        print("Wrong Guess!")
        print("Chances Left:", chances)

if chances == 0:
    print("Game Over!")
    print("The word was:", word)