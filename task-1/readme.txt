# Hangman Game

A simple command-line Hangman game written in Python.

## How to Play

1. Run the program: `python hangman.py`
2. The game will randomly select a word from a predefined list
3. Guess one letter at a time to reveal the word
4. You have **8 chances** to guess the word before losing
5. Win by revealing all letters before running out of chances

## Rules

- Enter only one letter per guess
- Letters can only be used once
- Correct guesses reveal the letter's position(s)
- Wrong guesses reduce your remaining chances

## Requirements

- Python 3.x
- No external libraries needed (uses built-in `random` module)

## Example

```
Welcome to Hangman!
You have 8 chances to guess the word.
Word: _ _ _ _ _
Enter a letter: a
Correct!
Word: a _ _ _ _
```

## Word List

Currently includes: apple, table, chair, snake, water

Feel free to add more words to the `words` list in the code!