with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

lstLength = len(content[0])
lst = [[] for _ in range(lstLength)]

for i in range(len(content)):
	for j in range(8):
		lst[j].append(content[i][j])

lst2 = lst[0]
for i in range(8):
	lst[i] = sorted(lst[i])

def countChars(lijst):
	uniqueChars = []
	countList = []
	for i in range(len(lijst)):
		if lijst[i] not in uniqueChars:
			uniqueChars.append(lijst[i])
			countList.append(lijst.count(lijst[i]))
	return uniqueChars, countList

def minChar(uniqueCharacters, countedChars):
	maxIndex = countedChars.index(min(countedChars))
	return uniqueCharacters[maxIndex]

code = ''
for k in range(lstLength):
	uniqueChars, countedChars = countChars(lst[k])
	minCharacter = minChar(uniqueChars,countedChars)
	code += minCharacter

print(code)