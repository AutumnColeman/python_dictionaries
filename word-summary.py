#Write a program to read in the text of that file and count the number of occurrences of each word in that file. You will print one line for each word encountered, and output the number of times that word appearred in the file.


#text = text.replace('.', '').replace('(', '').replace(')', '')

from sys import argv

script, filename = argv

blues = open(filename)

counts = {}

for char in blues.lower():
    text = char.replace('.', '').replace('(', '').replace(')', '')
    for word in char.split():
        counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
        print "%s: %d" % (word, counts[word])
