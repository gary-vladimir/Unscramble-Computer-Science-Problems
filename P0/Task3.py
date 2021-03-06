"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


receivers = []
for call in calls:
    if call[0].startswith("(080)"):  # caller is from Bangalore
        receivers.append(call[1])


codes = set()
for phone in receivers:
    if phone.startswith("(080)"):
        # Receiver is from Bangalore
        codes.add(phone[:5])
    elif phone.startswith("140"):
        # Receiver is a telemarketer
        codes.add(phone[:3])
    elif phone.startswith("(0"):
      # Receiver is a fixed_line
        codes.add(phone[0:phone.find(")")+1])
    elif phone.startswith(("7", "8", "9")):
        # Receiver is a mobile number
        codes.add(phone[:4])

print("The numbers called by people in Bangalore have codes:")
print('\n'.join(sorted(codes)))


# part B

numbers_from_bangalore_to_bangalore = []
for call in receivers:
    if call.startswith("(080)"):
        numbers_from_bangalore_to_bangalore.append(call)

percentage = (len(numbers_from_bangalore_to_bangalore)/len(receivers))*100
print(round(percentage, 2),  # 2 as for two decimal digits
      "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
