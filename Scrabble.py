_name_ = "Scrabble"
#Written by Dustin Brashear

#Assign default values
Double_Letter = [3, 9, 15, 21, 27, 33, 39]
Triple_Letter = [5, 10, 20, 25, 30, 35, 40]
Double_Word = [7, 14, 28]
Triple_Word = [8, 16, 24, 32]
Letter_Scores = {
                 'A': 1, 'E' : 1, 'D' : 2, 'R' : 2,
                 'B' : 3, 'M' : 3, 'V' : 4, 'Y' : 4,
                 'J' : 8, 'X' : 8
                 }
#prompt for word and remove commas and spaces
word = raw_input('Enter the word: ')
word = word.upper()
Word_List = [char for char in word if not (char == ',' or char == ' ')]

def process_Action(littlelist, wordlist): #turns a start pos. and a direction
    total = 0                             #into a score
    interval = 1
    multiple = 1
    start = int(littlelist[0])
    if littlelist[1] == 'V':
        interval = 10        
    places = []
    places.append(start)
    places.append(start + interval) 
    places.append(start + (2 * interval)) 
    places.append(start + (3 * interval))
    
    for x in xrange(4): #total the word
        letter = Letter_Scores.get(wordlist[x])
        if places[x] in Double_Letter:
            total += letter * 2
        elif places[x] in Triple_Letter:
            total += letter * 3
        else:
            total += letter
            
    for x in xrange(4): #figure out multiplier
        if places[x] in Double_Word:
            multiple = multiple * 2
        elif places[x] in Triple_Word:
            multiple = multiple * 3
    return (total * multiple)

def get_Score(actionlist):#generates score for each set of start pos and direction
    total = 0
    score1 = actionlist[0 : 2]
    score = process_Action(score1, Word_List)
    if score > total:
        total = score
    score2 = actionlist[2 : 4]
    score = process_Action(score2, Word_List)
    if score > total:
        total = score
    score3 = actionlist[4 : 6]
    score = process_Action(score3, Word_List)
    if score > total:
        total = score
    return total

for x in xrange(5): #prompts for set of scoring instructions
    action = raw_input('Enter three starting locations and directions: ')
    action = action.translate(None, " ")
    Action_List = action.split(",")
    print get_Score(Action_List)
    
        
