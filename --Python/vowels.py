a = "pingpong"

def vowel(word):
    count = 0
    for char in word:
        if char in "aeiouAEIOU":
            count += 1
    print(count)

vowel(a)
