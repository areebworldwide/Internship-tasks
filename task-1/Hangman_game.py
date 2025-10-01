import random

words = ["apple", "table", "chair", "snake", "water"]

word = random.choice(words)   # choose random word
guessed = ["_"] * len(word)   # blanks for word
wrong = 0
used_letters = []

print("Welcome to Hangman!")
print("You have 8 chances to guess the word.")
print("Word:", " ".join(guessed))

while wrong < 8 and "_" in guessed:   # changed 6 → 8
    guess = input("Enter a letter: ").lower()

    # check if user typed only 1 letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only ONE letter.")
        continue

    if guess in used_letters:
        print("You already tried that letter.")
        continue
    used_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        wrong += 1
        print("Wrong! Chances left:", 8 - wrong)   # also changed here

    print("Word:", " ".join(guessed))

if "_" not in guessed:
    print("You win! The word was:", word)
else:
    print("You lose! The word was:", word)
