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

calls09 = [item for item in calls if "09-2016" in item[2]]  # O(n)

call_max = calls09[0].copy()
call_max.extend((0, 0))
received_max = call_max.copy()

for item in calls09:  # O(n ^ 2) + O(7)
    call_sum = 0
    received_sum = 0
    for value in calls09:
        if value[0] == item[0]:
            call_sum += int(value[3])
        if value[1] == item[1]:
            received_sum += int(value[3])
    item.append(call_sum)
    item.append(received_sum)
    if call_sum > call_max[4]:
        call_max = item
    if received_sum > received_max[5]:
        received_max = item

max_phone = ""
max_time = 0
if sum(call_max[4:]) > sum(received_max[4:]):
    max_phone = call_max[0]
    max_time = sum(call_max[4:])
else:
    max_phone = received_max[0]
    max_time = sum(received_max[4:])

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_phone, max_time))
