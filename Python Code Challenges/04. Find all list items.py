def indexOfValue(originalList, value):
    resultList = []
    for x in range(len(originalList)):
        if type(originalList[x]) == list:
            for index in indexOfValue(originalList[x], value):
                resultList.append([x] + index)
        elif value == originalList[x]:
            resultList.append([x])
    return resultList

print(indexOfValue([1, [0, 1]], 1)) #[[0], [1, 1]]
print(indexOfValue([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2)) #[[0, 0, 1], [0, 1], [1, 1]]