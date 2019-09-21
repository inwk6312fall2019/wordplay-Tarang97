# Give me a word with three consecutive double letters. 
# I’ll give you a couple of words that almost qualify, but don’t. 
# For example, the word committee, c-o-m-m-i-t-t-e-e. 
# It would be great except for the ‘i’ that sneaks in there. 
# Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it would work. 
# But there is a word that has three consecutive pairs of letters and 
# to the best of my knowledge this may be the only word. Of course there are 
# probably 500 more but I can only think of one. What is the word?
def three_consecutive(s):
    i = 0
    count = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1

fin = open('words.txt')
count = 0
for word in fin:
    word = word.strip()
    if three_consecutive(word) == True:
        print(word)
        count += 1
print(count)