

# inputString = "10000"
# diskLength = 20

inputString = "00111101111101000"
diskLength = 35651584

def fillDisk(inputString):
    a = inputString
    b = ""
    
    for i in range(1, len(a)+1):
        if a[-i] == "0":
            b += "1"
        else:
            b += "0"

    a += '0'
    a += b
    return(a)

def calculateChecksum(inputString):
    s = inputString
    index = 0
    out = ""
    for j in range(0, len(s), 2):
        
        if s[j] == s[j+1]:
            out += "1"
        else:
            out += "0"
    return out

while len(inputString) < diskLength:
    inputString = fillDisk(inputString)


content = inputString[:diskLength]

checksum_content = calculateChecksum(content)



while len(checksum_content) % 2 == 0:
    checksum_content = calculateChecksum(checksum_content)

print(checksum_content)
