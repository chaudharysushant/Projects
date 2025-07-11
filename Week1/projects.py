word = input("Enter the word: ").lower()
cache = "_" * len(word)
attempts = 6
guessed_letters = []

print("\n" * 50) 

while attempts > 0 and cache != word:
    print("Current word:", cache)
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)
    new_cache = ""
    for index, letter in enumerate(word):
       
        if letter in guessed_letters:
            new_cache += letter
        else:
            new_cache += "_"
    cache = new_cache

    if guess not in word:
        attempts -= 1
        print("Wrong Guess. Attempts left:", attempts)

if cache == word:
    print("You guessed the word:", word)
else:
    print("Game over! The word was:", word)
