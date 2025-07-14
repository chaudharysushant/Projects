sentence = "banana apple banana cherry apple banana"
words = sentence.split()

word_freq = {word: words.count(word) for word in set(words)}
print(word_freq)
