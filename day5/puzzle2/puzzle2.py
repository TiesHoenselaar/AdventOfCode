import hashlib

puzzleInput = "abbhdwsy"

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

count = 0
i = 0
code = ['','','','','','','','']

listOfIndexes = []

while len(listOfIndexes) < 8:
	if computeMD5hash(puzzleInput + str(i))[0:5] == '00000':
		hashCode = computeMD5hash(puzzleInput + str(i))
		index = hashCode[5]
		if index.isdigit():
			if int(index) < 8 and int(index) not in listOfIndexes:
				code[int(index)] = hashCode[6]
				listOfIndexes.append(int(index))
		count += 1
	i += 1

password = ''.join(code)
print(password)