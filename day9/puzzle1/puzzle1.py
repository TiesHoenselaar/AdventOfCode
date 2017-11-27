with open("input.txt") as f:
    content = f.readlines()

testString = content[0]
index = 0
tmp = -1
tmp2 = -1

newString = ''
while index < len(testString):
	newString += testString[index]

	if testString[index] == '(':
		tmp = index
	if testString[index] == ')':
		tmp2 = index

	if tmp != -1 and tmp2 != -1:
		marker = testString[tmp+1:tmp2]
		newString = newString[:-(len(marker)+2)]
		markerClean = marker.split('x')
		repeat = testString[tmp2+1:tmp2+int(markerClean[0])+1]
		for i in range(int(markerClean[1])):
			newString += repeat
		tmp = -1
		tmp2 = -1
		index += int(markerClean[0])
	index += 1

print(len(newString))