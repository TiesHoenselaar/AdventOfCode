from math import floor

numOfElves = 5
elves = list(range(1,numOfElves+1))

currentElf = 0

skip = floor(len(elves)/2)
idx = skip

while len(elves) > 1:
    (elves.pop(idx))
    idx = (idx + skip) % len(elves)
    skip = floor(len(elves)/2)

print(elves)

# 221754 too low