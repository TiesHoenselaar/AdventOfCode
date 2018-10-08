def next_num(number):
    return (number*252533)%33554393

count = 1

row = 1
col = 1

row_target = 3010
col_target = 3019

while (row, col) != (row_target, col_target):
    if row != 1:
        row -= 1
        col += 1
    else:
        row = col + 1
        col = 1
    count += 1

number = 20151125

for i in range(count - 1):
    number = next_num(number)

print(number)