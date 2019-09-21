#Write a function named avoids that takes a word and a string of forbidden letters, 
#and that returns True if the word doesn’t use any of the forbidden letters.
def avoids(word, forbidletters):
    for letter in word:
        if letter in forbidletters: #if 'aeronautical' in 'aeiou'
            return False
        return True
word = input('Enter any string: ') #For ex: aeronautical
letters = input('Enter any characters: ') #For ex: aeiou
print(avoids(word,letters)) #avoids(aeronautical, aeiou)

#Write a program that prompts the user to enter a string of forbidden letters 
#and then prints the number of words that don’t contain any of them. 
#Can you find a combination of 5 forbidden letters that excludes the smallest 
#number of words?
fin = open('words.txt')
count = 0
forbidden_letters = input('Enter any forbidden letters: ')
for line in fin:
    word = line.strip()
    if avoids(word, forbidden_letters) == True:
        count += 1
print(count)

