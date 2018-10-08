
fname = "input.txt"
with open(fname) as f:
    data = f.read()

program = data.split("\n")

# print(program)


regs = {'a' :  1, 'b' : 0}
i = 0

while i < len(program) and i >= 0:

    instruction, r = program[i].split(' ', 1)
    di = 1

    if instruction == "hlf":
        regs[r] //= 2
    elif instruction == "tpl":
        regs[r] *= 3
    elif instruction == "inc":
        regs[r] += 1
    elif instruction == "jmp":
        di = int(r)
    elif instruction == "jie":
        r, offset = r.split(",")
        if regs[r] % 2 == 0:
            di = int(offset)
    elif instruction == "jio":
        r, offset = r.split(",")
        if regs[r] == 1:
            di = int(offset)
    
    i += di

print(regs)