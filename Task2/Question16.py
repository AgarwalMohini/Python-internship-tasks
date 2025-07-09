#Count vowels and consonants

s = input().lower()
vowels = {'a', 'e', 'i', 'o', 'u'}
count_vowels = 0
count_consonants = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            count_vowels += 1
        else:
            count_consonants += 1

print(count_vowels, count_consonants)
