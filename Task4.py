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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers = [item[0] for item in calls]  # O(n)
text_receivers = [item[1] for item in texts]  # O(n)
call_receivers = [item[1] for item in calls]  # O(n)
telemarketers = set([item[0] for item in calls if item[0] not in text_receivers and item[0] not in call_receivers])  # O(n)

telemarketers = list(telemarketers)  # O(1)

telemarketers.sort()  # O(n log n)

print("These numbers could be telemarketers: ")  # O(1)
print("\n".join(telemarketers))  # O(n)
