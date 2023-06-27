def saveDictionary(dict, filePath):
    file = open(filePath, "w")
    file.write(str(dict))
    file.close

def loadDictionary(filePath):
    result = {}
    file = open(filePath, "r")
    text = str(file.read())
    pairs = text.replace("{", "").replace("}", "").split(", ")
    for pair in pairs:
        keyValue = pair.split(": ")
        result.update({keyValue[0].replace("'", ""): keyValue[1].replace("'", "")})
    print(result)
    return result

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
saveDictionary(thisdict, r"Python Code Challenges\resources\dict.txt")
newDict = loadDictionary(r"Python Code Challenges\resources\dict.txt")
print(thisdict["brand"])
print(newDict["brand"])