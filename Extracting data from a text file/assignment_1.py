...
Write a program to read text file (mbox-short.txt) and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
...

name = input("Enter file:")
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        pieces = words[1]
        counts[pieces] = counts.get(pieces, 0) + 1

largest = -1
bigword = None

for pieces,value in counts.items():
    if value > largest:
        largest = value
        bigword = pieces

print(bigword, largest)
