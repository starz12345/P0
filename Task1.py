"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import time
import csv
start = time.time()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

tele = set()
for item in texts:
    tele.add(item[0])
    tele.add(item[1])
for item in calls:
    tele.add(item[0])
    tele.add(item[1])
print("There are {} different telephone numbers in the records.".format(len(tele)))

end = time.time()
print("{:.2f} seconds".format(end - start))


