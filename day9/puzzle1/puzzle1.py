with open("input.txt") as f:
    content = f.readlines()

# print(content[0])


testString = 'A(1x5)BC'
# testString = '(3x3)XYZ'
index = 0
tmp = -1
tmp2 = -1

newString = ''
while index < len(testString):
	
	if testString[index] == '(':
		tmp = index
	if testString[index] == ')':
		tmp2 = index
	if tmp != -1 and tmp2 != -1:
		marker = testString[tmp+1:tmp2].split('x')
		repeat = testString[tmp2+1:tmp2+int(marker[0])+1]
		for i in range(int(marker[1])):
			newString += repeat
		tmp = -1
		tmp2 = -1
	newString += testString[index]
	index += 1

print(newString)