'''
Requirements
35.	Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 500, and 1000 ) against an given amount
'''

# variables used
amount = 12680
count1000  = 0
count500 = 0

notesCountDict = {
    1000: 0, 
    500: 0, 
    100: 0,
    50: 0,
    20: 0,
    10: 0
}

# logic used
def notes_Counter(amnt, notes = {}):
    for k, v in notes.items():
        while amnt > 0:
            if amnt >= k:
                amnt -= k
                notes[k] += 1
            else:
                break
    return notes


# print output
for k, v in notes_Counter(amnt= amount, notes= notesCountDict).items():
    print("required {x} notes of {y}".format(x = v, y = k))

