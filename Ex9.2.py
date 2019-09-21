#Write a function called has_no_e that returns True 
#if the given word doesn’t have the letter “e” in it.
fin = open('words.txt')
def has_no_e():
    for word in fin:
        word = word.strip()
        if word.find('e') == -1:
            return True
        else:
            return False
print(has_no_e())

#Write a program that reads words.txt and prints only the words that have no “e”. 
#Compute the percentage of words in the list that have no “e”. 
file = open('words.txt')
number_of_words = 0
count = 0
for line in file:
    number_of_words += 1
    word = line.strip()
    if word.find('e') == -1:
        print(word)
        count += 1
    percent_of_words = (count/number_of_words) * 100
    print('Percent: ',percent_of_words)