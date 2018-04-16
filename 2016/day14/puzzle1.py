import hashlib

salt = "ngcjuoqr"


def createHash(key):
    return hashlib.md5(key.encode('utf-8')).hexdigest()

def containtsTriplet(hashCode):
    i = 0
    while(i < len(hashCode)-2):
        if hashCode[i] == hashCode[i+1] == hashCode[i+2]:
            return hashCode[i] 
        i += 1
    return -1

def containtsQuintet(hashCode, character):
    i = 0
    while(i < len(hashCode)-4):
        if hashCode[i] == hashCode[i+1] == hashCode[i+2] == hashCode[i+3] == hashCode[i+4] == character:
            return 1
        i += 1
    return 0

count = 0
index = 0

while count < 64:
    hashCode = createHash(salt + str(index))
    while containtsTriplet(hashCode) == -1:
        index += 1
        hashCode = createHash(salt + str(index))

    character = containtsTriplet(hashCode)

    for i in range(index + 1, index + 1001):
        if containtsQuintet(createHash(salt+str(i)),character):
            count += 1
            print("count:", count, "character:", character, "index: ", index)
            break

    index += 1


print("count:", count)