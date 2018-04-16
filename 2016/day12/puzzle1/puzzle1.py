fname = "input.txt"

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

a,b,c,d = 0,0,1,0



lineNumber = 0

while lineNumber >= 0 and lineNumber < len(content):
    line = content[lineNumber]
    lineSplitted = line.split()
    # print("Before a:{}, b:{}, c:{}, d:{}  line {}: {}".format(a,b,c,d,lineNumber, line))
    
    # COPY
    if lineSplitted[0] == "cpy":
        value = lineSplitted[1]
        if value == "a":
            copyValue = a
        elif value == "b":
            copyValue = b
        elif value == "c":
            copyValue = c
        elif value == "d":
            copyValue = d
        else:
            copyValue = int(value)        
        
        reg = lineSplitted[2]
        if reg == "a":
            a = copyValue
        elif reg == "b":
            b = copyValue
        elif reg == "c":
            c = copyValue
        elif reg == "d":
            d = copyValue

        lineNumber += 1

    # INCREASE
    elif lineSplitted[0] == "inc":
        reg = lineSplitted[1]
        if reg == "a":
            a += 1
        elif reg == "b":
            b += 1
        elif reg == "c":
            c += 1
        elif reg == "d":
            d += 1

        lineNumber += 1

    # DECREASE
    elif lineSplitted[0] == "dec":
        reg = lineSplitted[1]
        if reg == "a":
            a -= 1
        elif reg == "b":
            b -= 1
        elif reg == "c":
            c -= 1
        elif reg == "d":
            d -= 1

        lineNumber += 1

    # JUMP IF NOT ZERO
    elif lineSplitted[0] == "jnz":
        jump = True
        reg = lineSplitted[1]

        if reg == "a":
            if a == 0: jump = False
        elif reg == "b":
            if b == 0: jump = False
        elif reg == "c":
            if c == 0: jump = False
        elif reg == "d":
            if d == 0: jump = False

        if jump:
            lineNumber += int(lineSplitted[2])
        else:
            lineNumber += 1
        
print("After  a:{}, b:{}, c:{}, d:{} \n".format(a,b,c,d))


# 2796 too low