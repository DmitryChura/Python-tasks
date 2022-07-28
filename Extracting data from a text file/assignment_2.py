"""
Write a program to read through the text file (we use mbox-short.txt) and figure out the distribution by hour of the day for each of the messages.
The program looks for 'From ' lines like "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008".
Once you have accumulated the counts for each hour, print out the counts, sorted by hour.
"""

name = input("Enter file:")
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        pieces = words[5]
        times = pieces.split(':')
        hour = times[0]
        if hour in counts: 
            counts[hour] = counts[hour] + 1
        else:
            counts[hour] = 1
            
for hour, value in sorted(counts.items()):
    print("hour:", hour, 'count:', value)

"""
Input:
mbox-short.txt

Output:
hour: 04 count: 3
hour: 06 count: 1
hour: 07 count: 1
hour: 09 count: 2
hour: 10 count: 3
hour: 11 count: 6
hour: 14 count: 1
hour: 15 count: 2
hour: 16 count: 4
hour: 17 count: 2
hour: 18 count: 1
hour: 19 count: 1
"""
