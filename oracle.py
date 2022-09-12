import random
import msvcrt

"""
structure of maps is : 

map_5gram = {
    "fddfd" : { f : 1, d : 2},
    "dddfd" : { f : 3, d : 1}
}

"""

map_5gram = {}
map_4gram = {}
map_3gram = {}

stream = ""
curr = ""

total_guesses = 0
three_correct = 0
four_correct = 0
five_correct = 0

five_predict = ""
four_predict = ""
three_predict = ""

while(True):
    # take input
    # curr = input("Enter f or d : ")
    print("Enter f or d : ")
    curr = msvcrt.getch().decode('ASCII')

    if curr == 'p' :
        break

    while (curr != 'f' and curr != 'd'):
        # curr = input("please enter only f or d : ")
        print("Please enter only f or d : ")
        curr = msvcrt.getch().decode('ASCII')
        if curr == 'p' :
            break

    if curr == 'p' :
        break

    # add to stream
    stream += curr

    # check if enough info is there to predict
    if len(stream) <= 6:
        print("Too little data to predict right now")
        print()
        print("-----------------------------------------------")
        print()
        continue

    # check if last prediction was correct
    if five_predict == "" or four_predict == "" or three_predict == "":
        print("No predictions this round.")
    else :
        # check stats for each type
        total_guesses += 1
        if five_predict == curr:
            five_correct += 1
        if four_predict == curr:
            four_correct += 1
        if three_predict == curr:
            three_correct += 1
        
        # show user the output
        print("You : {}. 5gram : {}. 4gram : {}. 3gram : {}".format(curr, five_predict, four_predict, three_predict))
        print("5gram pct : {}, 4gram pct : {}, 3gram pct : {}".format(round(five_correct*100/total_guesses, 2), round(four_correct*100/total_guesses, 2), round(three_correct*100/total_guesses, 2)))

    # add this to 5 gram, 4 gram, 3 gram
    five_gram = stream[-6:-1]
    four_gram = stream[-5:-1]
    three_gram = stream[-4:-1]

    # 5gram
    if five_gram in map_5gram.keys() :
        map_5gram[five_gram][curr] += 1
    else:
        freq_dict = {}
        freq_dict["f"] = 0
        freq_dict["d"] = 0
        freq_dict[curr] += 1
        map_5gram[five_gram] = freq_dict

    # 4gram
    if four_gram in map_4gram.keys() :
        map_4gram[four_gram][curr] += 1
    else:
        freq_dict = {}
        freq_dict["f"] = 0
        freq_dict["d"] = 0
        freq_dict[curr] += 1
        map_4gram[four_gram] = freq_dict

    # 3gram
    if three_gram in map_3gram.keys() :
        map_3gram[three_gram][curr] += 1
    else:
        freq_dict = {}
        freq_dict["f"] = 0
        freq_dict["d"] = 0
        freq_dict[curr] += 1
        map_3gram[three_gram] = freq_dict

    # make predictions for next round
    five_gram = stream[-5:]
    four_gram = stream[-4:]
    three_gram = stream[-3:]

    # generate random predictor
    a = random.randint(0, 1)
    guess = ""
    if a == 0 :
        guess = "f"
    else :
        guess = "d"

    # using 5gram
    if five_gram not in map_5gram.keys():
        freq_dict = {}
        freq_dict["f"] = 0
        freq_dict["d"] = 0
        map_5gram[five_gram] = freq_dict

    if map_5gram[five_gram]["f"] > map_5gram[five_gram]["d"]:
        five_predict = "f"
    elif map_5gram[five_gram]["f"] < map_5gram[five_gram]["d"]:
        five_predict = "d"
    else : 
        five_predict = guess

    # using 4gram
    if four_gram not in map_4gram.keys():
        freq_dict = {}
        freq_dict["f"] = 0
        freq_dict["d"] = 0
        map_4gram[four_gram] = freq_dict

    if map_4gram[four_gram]["f"] > map_4gram[four_gram]["d"]:
        four_predict = "f"
    elif map_4gram[four_gram]["f"] < map_4gram[four_gram]["d"]:
        four_predict = "d"
    else : 
        four_predict = guess
    
    # using 3gram
    if three_gram not in map_3gram.keys():
        freq_dict = {}
        freq_dict["f"] = 0
        freq_dict["d"] = 0
        map_3gram[three_gram] = freq_dict

    if map_3gram[three_gram]["f"] > map_3gram[three_gram]["d"]:
        three_predict = "f"
    elif map_3gram[three_gram]["f"] < map_3gram[three_gram]["d"]:
        three_predict = "d"
    else : 
        three_predict = guess

    # show output, compute accuracy

    # clear line for next input

    print()
    print("-----------------------------------------------")
    print()
