word_freq = {}

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(word_freq)