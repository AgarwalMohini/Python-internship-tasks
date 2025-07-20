#Check anagram

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Input
s1 = input("Enter first string: ").strip()
s2 = input("Enter second string: ").strip()

print(is_anagram(s1, s2))
