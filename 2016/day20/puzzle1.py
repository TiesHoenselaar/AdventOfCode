
record = []
with open("input.txt", mode="r") as f:
    content = f.readlines()
    

for i in range(len(content)):
    a,b = content[i].strip().split("-")
    record.append((int(a),int(b)))

record.sort()

total, ip, index = 0, 0, 0

while ip < 2**32:
    lower, upper = record[index]
    if ip >= lower:
        if ip <= upper:
            ip = upper + 1
            continue
        index += 1
    else:
        total += 1
        ip += 1

print(total)