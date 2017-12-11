listLength = 5
# listLength = 256

inputLengths = [3, 4, 1, 5]
# inputLengths = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]

l = []
for i in range(listLength):
	l.append(i)

pos = 0
skipSize = 0

for i in range(len(inputLengths)):
# for i in range(5):
	skipAmount = inputLengths[i] + skipSize
	if (pos + skipAmount)%len(l) >= pos:
		subList = l[pos:pos+skipAmount]
		l[pos:pos+skipAmount] = (l[pos:pos+skipAmount])[::-1]
		# print(l)
	else:

		subList = l[pos:] + l[:(pos+skipAmount)%len(l)-1]
		reversedList = subList[::-1]
		# print(reversedList)

		# l[pos:] = (reversedList[:len(l[pos:])])
		# l[:(pos+skipAmount)%len(l)-1] = (reversedList[(pos+skipAmount)%len(l)-1:])

		l[:(pos+skipAmount)%len(l)-1] = (reversedList[:len(l[pos:])])
		l[pos:] = (reversedList[(pos+skipAmount)%len(l)-1:])

	print(l)

		# print(subList)

	pos = (pos+skipAmount)%len(l)
	skipSize += 1



