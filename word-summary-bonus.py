#Write a program to read in the text of that file and count the number of occurrences of each word in that file. You will print one line for each word encountered, and output the number of times that word appearred in the file.  Print the top 10 most frequently used words in the file
from sys import argv

script, filename = argv

blues = open(filename)

counts = {}

for char in blues:
    text = char.replace('.', '').replace('(', '').replace(')', '')
    for word in char.split():
        counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
        top_10 = counts.sort()
        while i < 10:
            print top_10.pop()
            break
        #print "%s: %d" % (word, counts[word])

blues.close()
