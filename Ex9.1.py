#Write a program that reads words.txt and 
#prints only the words with more than 20 
#characters (not counting whitespace).
fin = open('words.txt')
for word in fin:
    word = word.strip()
    if len(word) > 20:
        print(word)