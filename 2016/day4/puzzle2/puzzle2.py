def shiftLetter(char, shift):
	charNumber = ord(char) - 97
	charNumberShifted = ( charNumber + (shift % 26) ) % 26
	charShifted = chr(charNumberShifted + 97)
	return charShifted

with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
	words = ''
	name = (content[i].split("[",)[0].split("-")[0:-1])
	shift = int(content[i].split("[",)[0].split("-")[-1])
	for j in range(len(name)):
		word = ''
		for k in range(len(name[j])):
			word += shiftLetter(name[j][k],shift)
		words += (word + ' ')
	print(words[0:-1], shift)