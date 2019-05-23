"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

calls09 = [item for item in calls if "09-2016" in item[2]] #O(n)

callers = dict()
max_phone, max_calls = "", 0

for item in calls09: #O(n)
    callers[item[0]] = callers.get(item[0], 0) + int(item[3])
    callers[item[1]] = callers.get(item[1], 0) + int(item[3])

    if callers[item[0]] > max_calls:
        max_phone, max_calls = item[0], callers[item[0]]

    if callers[item[1]] > max_calls:
        max_phone, max_calls = item[1], callers[item[1]]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_phone, max_calls))
