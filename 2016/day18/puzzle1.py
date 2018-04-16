row = "^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^"

rows = [[x=="." for x in row]]

# print(sum(rows[0]))

def nextRow(rows):
    prevRow = rows[-1]
    currentRow = []

    for i in range(len(prevRow)):
        if i == 0:
            left = True
        else:
            left = prevRow[i-1]

        center = prevRow[i]

        if i == len(prevRow)-1:
            right = True
        else:
            right = prevRow[i+1]
        
        # print(left,center,right)

        safe = True

        if not left and not center and right:
            safe = False
        if left and not center and not right:
            safe = False
        if not left and center and right:
            safe = False
        if left and center and not right:
            safe = False
    
        currentRow.append(safe)

    return currentRow



total_rows = 400000

for i in range(total_rows-1):
    rows.append(nextRow(rows))


total = 0
for j in range(total_rows):
    total += sum(rows[j])

print(total)
