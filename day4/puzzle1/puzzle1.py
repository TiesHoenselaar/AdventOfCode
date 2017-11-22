
# print("checksum:\t{0}".format(checksum))
# print("sectorID:\t{0}".format(sectorID))
# print("name:\t\t{0}".format(name))

def uniqueCharacters(string):
	unique = []
	for i in range(len(string)):
		if string[i] not in unique:
			unique.append(string[i])
	return unique

def countCharacters(string, uniqueChars):
	countChars = []
	for i in range(len(uniqueChars)):
		countChars.append(string.count(uniqueChars[i]))
	return countChars

def testName(string):
	checksum = string.split("[",)[1][:-1]
	sectorID = int(string.split("[",)[0].split("-")[-1])
	name = ''.join(sorted(''.join(string.split("[",)[0].split("-")[0:-1])))

	uniqueChars = uniqueCharacters(name)
	countChars = countCharacters(name,uniqueChars)

	check = ''
	for i in range(5):
		index = countChars.index(max(countChars))
		check += uniqueChars[index]
		countChars.pop(index)
		uniqueChars.pop(index)

	if checksum == check:
		return sectorID
	else:
		return 0

counter = 0

with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

for k in range(len(content)):
	counter += testName(content[k])


print(counter)
