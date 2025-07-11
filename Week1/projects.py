word = input("Enter the word: ")
cache = "_" * len(word)
attempts = 6
guessed_letters = []

while attempts > 0 and cache != word:
    print("Current word:", cache)
    guess = input("Guess a letter: ")
    guessed_letters.append(guess)
    new_cache = ""
    for index, letter in enumerate(word):
        print(f"{index}: {letter}")
        if letter in guessed_letters:
            new_cache += letter
        else:
            new_cache += "_"
    cache = new_cache
    if guess not in word:
        attempts -= 1
