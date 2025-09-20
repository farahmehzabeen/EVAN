import random

# 1. Secret Word Reveal
word = "mystery"
print("1. Secret Word Reveal")
print("First and Last:", word[0] + word[-1])
print("Reversed:", word[::-1])
print("Vowels Replaced:", ''.join(['*' if c in 'aeiouAEIOU' else c for c in word]))
print()

# 2. Repeat Name Pyramid
print("2. Repeat Name Pyramid")
name = "Farah"
for i in range(len(name), 0, -1):
    print(name[:i])
print()

# 3. Dice Game
print("3. Dice Game")
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2
print("You rolled:", die1, "and", die2)
if total in (7, 11):
    print("You win!")
elif die1 == die2:
    print("Double trouble!")
else:
    print("Total:", total)
print()

# 4. Swap Case Message
print("4. Swap Case Message")
msg = "Python Is Fun!"
print("Upper:", msg.upper())
print("Lower:", msg.lower())
print("Swapped:", msg.swapcase())
print()

# 5. Middle Character
print("5. Middle Character")
word = "banana"
length = len(word)
if length % 2 == 0:
    print("Middle characters:", word[length//2 - 1:length//2 + 1])
else:
    print("Middle character:", word[length//2])
print()

# 6. Count Letters
print("6. Count Letters")
sentence = "Hello World"
counts = {}
for c in sentence.lower():
    if c.isalpha():
        counts[c] = counts.get(c, 0) + 1
print(counts)
print()

# 7. Name Masker
print("7. Name Masker")
full_name = "Farah Mehzabeen"
masked = ' '.join([n[0] + '*' * (len(n) - 1) for n in full_name.split()])
print("Masked Name:", masked)
print()

# 8. Word Length Filter
print("8. Word Length Filter")
sentence = "This is a simple Python exercise to practice."
long_words = [word for word in sentence.split() if len(word) > 4]
print("Words longer than 4 letters:", long_words)
print()

# 9. Multiply List Numbers
print("9. Multiply List Numbers")
nums = [1, 4, 7, 10]
result = [n * 3 for n in nums]
print("Multiplied by 3:", result)
print()

# 10. Mirror Sentence
print("10. Mirror Sentence")
sentence = "I like pizza"
reversed_sentence = ' '.join(sentence.split()[::-1])
print("Reversed sentence:", reversed_sentence)
