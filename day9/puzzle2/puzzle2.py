with open("input.txt") as f:
    content = f.readlines()


# inputString = content[0]


inputString = 'X(8x2)(3x3)ABCY'
# inputString = 'A(1x5)BC'
# print(inputString)

def getMarker(string):
	start = -1
	end = -1
	for i in range(len(string)):
		if string[i] == '(':
			start = i
		if string[i] == ')':
			end = i
		if start != -1 and end != -1:
			marker = string[start+1:end].split('x')
			print(marker)
			characters = string[end+1:end+int(marker[0])+1]
			repeat = int(marker[1])
			
			return characters, repeat

			return 1
	return -1


def decryptString(woord):
	print(woord)
	a = woord.find('(')
	print(a)

woord = "(3x3)ABC(3x3)ABC"

decryptString(woord)


# tmpString = ''

# counter = 0
# index = 0

# while index < len(inputString):
# 	if inputString[index] == '(':
# 		chars,repeat = getMarker(inputString[index:])
# 		# print(chars)
# 		tmpString = repeat*chars
# 		print(tmpString)
# 	else:
# 		counter += 1

# 	index += 1





# testString = '(3x3)XYZ'
index = 0
tmp = -1
tmp2 = -1

# newString = ''
# while index < len(testString):
	
# 	if testString[index] == '(':
# 		tmp = index
# 	if testString[index] == ')':
# 		tmp2 = index
# 	if tmp != -1 and tmp2 != -1:
# 		marker = testString[tmp+1:tmp2].split('x')
# 		repeat = testString[tmp2+1:tmp2+int(marker[0])+1]
# 		for i in range(int(marker[1])):
# 			newString += repeat
# 		tmp = -1
# 		tmp2 = -1
# 	newString += testString[index]
# 	index += 1

# print(newString)