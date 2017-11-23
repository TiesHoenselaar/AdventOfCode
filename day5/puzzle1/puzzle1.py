import hashlib

puzzleInput = "abbhdwsy"

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

count = 0
i = 0
password = ''

while count < 8:
	if computeMD5hash(puzzleInput + str(i))[0:5] == '00000':
		password += str(computeMD5hash(puzzleInput + str(i))[5])
		count += 1
	i += 1

print(password)