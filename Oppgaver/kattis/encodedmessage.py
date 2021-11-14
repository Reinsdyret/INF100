"""https://open.kattis.com/problems/encodedmessage"""
import math

def encode_message(message:str) -> str:
    side_length = int(math.sqrt(len(message)))
    original_table = []
    row = []
    for i in range(len(message)):
        if i % side_length == 0 and i != 0:
            original_table.append(row)
            row = []
        row.append(message[i])
    original_table.append(row)
    rotated_table = list((list(zip(*list((list(zip(*list(reversed(list(zip(*original_table))))))))))))
    for i in range(len(rotated_table)):
        rotated_table[i] = list(rotated_table[i])
    original_message = ''.join(str(item) for innerlist in rotated_table for item in innerlist)
    
    

    return original_message

n = int(input())
messages = []
new_messages = []

for i in range(n):
    messages.append(input())

for message in messages:
    new_messages.append(encode_message(message))

for new_message in new_messages:
    print(new_message)