memoryBank = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
#memoryBank = [0, 2, 7, 0]

memoryBanks = []


def redistribute(memoryBank):
	maxAmount = max(memoryBank)
	maxIndex = memoryBank.index(maxAmount)


	memoryBank[maxIndex] = 0
	
	for i in range(maxAmount):
		memoryBank[(maxIndex + i + 1)%len(memoryBank)] += 1
	return memoryBank

counter = 0
while memoryBank not in memoryBanks:
	memoryBanks.append(memoryBank[:])
	memoryBank = redistribute(memoryBank)
	counter += 1

print(counter)
print(counter - memoryBanks.index(memoryBank))

