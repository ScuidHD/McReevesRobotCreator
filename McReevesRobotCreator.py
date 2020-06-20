import random
that = [
"delivers butter",
"washes the dishes",
"makes other robots",
"shoots at people",
"tazes you",
"electrifies you",
"shoots",
"dispenses paper",
"screams",
"says something messed up",
"dresses you",
"shoots straws at people",
"hits you",
"that throws everything its holding on the floor",
"poops cereal",
"moans",
"kills itself",
"throws ok boomer cards at lily",
"kills a person",
"washes peoples faces"]

that2 = [
"delivers butter",
"that throws everything its holding on the floor",
"washes the dishes",
"makes other robots",
"shoots at people",
"tazes you",
"electrifies you",
"shoots",
"dispenses paper",
"screams",
"says something messed up",
"dresses you",
"shoots straws at people",
"hits you",
"poops cereal",
"moans",
"kills itself",
"throws ok boomer cards at lily",
"kills a person"
"washes peoples faces"]


whenever = [
"you step on it",
"you scream",
"you cough",
"you loose health in a game",
"it recognizes a face",
"you pull a trigger",
"you walk slow",
"one hour passes",
"it sees a robot idea",
"it sees movement",
"you press a button",
"you drink something",
"you type",
"you click your mouse",
"you open a door",
"you try to open it",
"you switch it off",
]

while True:

    hiii = input("how much things? 1 or 2 or exit: ")

    z1 = random.randint(0, len(that)-1)
    z2 = random.randint(0, len(whenever)-1)
    z3 = random.randint(0, len(that2)-1)

    

    if hiii == "1":
        print ("Make a robot that", that[z1], "whenever", whenever[z2])
    elif hiii == "2":
        print ("Make a robot that", that[z1], "and", that2[z3], "whenever", whenever[z2])
    elif hiii == "exit":
        break
    else:
        print ("please enter 1 or 2 or exit.")




