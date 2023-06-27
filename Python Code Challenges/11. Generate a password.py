import random

def generatePassphrase(nbr):
    file = open(r"Python Code Challenges\resources\dicewarewordlist.txt", "r")
    text = str(file.read())
    dict = {}
    pairs = text.split("\n")
    for pair in pairs:
        keyValue = pair.split("\t")
        dict.update({keyValue[0]: keyValue[1]})
    result = ""
    for x in range(1, nbr + 1):
        passcode = ""
        for i in range(1, 6):
            passcode += str(random.randint(1, 6))
        print(passcode)
        
        result += " " + dict.get(passcode)
    return result.strip()


print(generatePassphrase(5))