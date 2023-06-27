def sortString(text):
    words = text.split(" ")
    words.sort(key = lambda w: w.upper())
    return words

print(sortString("banana ORANGE apple")) #['apple', 'banana', 'ORANGE']