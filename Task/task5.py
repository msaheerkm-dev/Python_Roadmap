stri = input("Enter a string: ").replace(" ", "").lower()

vowels = set("aeiou")
consonants = set("bcdfghjklmnpqrstvwxyz")

count_vowel = 0
count_cons = 0

for ch in stri:
    if ch in vowels:
        count_vowel += 1
    elif ch in consonants:
        count_cons += 1

print("vowel count:", count_vowel)
print("consonants count:", count_cons)
