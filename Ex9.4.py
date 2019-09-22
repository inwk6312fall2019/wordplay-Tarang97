#Write a function named uses_only that takes a word and a string of letters, 
#and that returns True if the word contains only letters in the list. 
#Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa”?
def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

fin = open('words.txt')
count = 0
for line in fin:
    word = line.strip()
    if uses_only(word, 'acefhlo') == True:
        print(word)
        count += 1
print(count)
