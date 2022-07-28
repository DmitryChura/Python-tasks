Write a program to read text file (file_1.txt) and figure out who has sent the greatest number of mail messages.

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
