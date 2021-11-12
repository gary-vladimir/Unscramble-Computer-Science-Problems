"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

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

telemarketers = []

outgoing_calls = set()
incoming_calls = set()
for call in calls:
    outgoing_calls.add(call[0])
    incoming_calls.add(call[1])

outgoing_texts = set()
incoming_texts = set()
for text in texts:
    outgoing_texts.add(call[0])
    incoming_texts.add(call[1])


for phone in outgoing_calls:
    if (phone not in outgoing_texts) and (phone not in incoming_texts) and (phone not in incoming_calls):
        telemarketers.append(phone)


telemarketers.sort()
print("These numbers could be telemarketers: ")
for phone in telemarketers:
    print(phone)
