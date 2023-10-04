import random

def choose_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    with open('random_words.txt', 'r') as file:
        words = file.read().split(",")

    word_list = [word.strip() for word in words]
    target_word = choose_random_word(word_list)
    remaining_attempts = 10
    guessed_letters = []

    print("Welcome to 07_Hangman!")
    print(display_word(target_word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in target_word:
            remaining_attempts -= 1
            print(f"You got {remaining_attempts} remaining attempts left!")

        word_display = display_word(target_word, guessed_letters)
        print(word_display)

        if word_display == target_word:
            print("Congratulations! You won.")
            break

        if remaining_attempts == 0:
            print("You're out of attempts. The word was:", target_word)
            break


if __name__ == "__main__":
    hangman()



