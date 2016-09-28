#Write a program to read in the text of that file and count the number of occurrences of each word in that file. You will print one line for each word encountered, and output the number of times that word appearred in the file.  Print the top 10 most frequently used words in the file
from sys import argv

script, filename = argv

blues = open(filename)

counts = {}

for char in blues:
    text = char.replace('.', '').replace('(', '').replace(')', '')
    for word in char.split():
        counts[word] = counts.get(word, 0) + 1

entries = counts.items()

entries.sort(key=lambda entry: entry[1], reverse=True)

top_10 = entries[:10]

for word, count in top_10:
    print "%s appeared in %d times." % (word, count)

blues.close()
