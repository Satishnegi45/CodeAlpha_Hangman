import random

words = ["iphone", "oneplus", "jaguar", "coding", "congratulation"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 35)
print("          HANGMAN GAME")
print("=" * 35)

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nword:", display_word)
    print("wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    if all(letter in guessed_letters for letter in word):
        print("\n🎉 congratulations!")
        print("you guessed the word:", word)
        break

    guess = input("enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("you already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("good guess!")
    else:
        wrong_guesses += 1
        print("wrong guess!")

else:
    print("\n❌ game over!")
    print("the word was:", word)

print("\nthank you for playing!")