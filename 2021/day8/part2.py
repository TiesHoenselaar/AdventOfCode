from itertools import permutations

def difference(str1, str2):
    if len(str1) > len(str2):
        for letter in str1:
            if letter not in str2:
                return letter
    else:
        for letter in str2:
            if letter not in str1:
                return letter

with open ('input.txt') as f:
    lines = f.read().splitlines()

total = 0

for line in lines:
    ##x = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

    line = line.split(' ')

    input_values = line[:-5]
    output_values = line[-4:]

    sorted_input_values = [sorted(string) for string in input_values]
    #print(sorted_input_values)

    one_digits = [digit for digit in input_values if len(digit) == 2][0]
    four_digits = [digit for digit in input_values if len(digit) == 4][0]
    seven_digits = [digit for digit in input_values if len(digit) == 3][0]
    eight_digits = [digit for digit in input_values if len(digit) == 7][0]

    horizontal_up = difference(one_digits, seven_digits)

    #print(horizontal_up)

    letters = ['a','b','c','d','e','f','g']
    positions = [0, 1, 2, 3, 4, 5, 6]

    #positions = [0,1,2]

    combinations = permutations(positions, len(positions))

    bingo = False

    for comb in combinations:

        if not bingo:
            #print(comb)

            temp_zero = letters[comb[0]] + letters[comb[2]] + letters[comb[5]] + letters[comb[6]] + letters[comb[4]] + letters[comb[1]]
            temp_one = letters[comb[2]] + letters[comb[5]]
            temp_two = letters[comb[0]] + letters[comb[2]] + letters[comb[3]] + letters[comb[4]] + letters[comb[6]]
            temp_three = letters[comb[0]] + letters[comb[2]] + letters[comb[5]] + letters[comb[6]] + letters[comb[3]]
            temp_four = letters[comb[1]] + letters[comb[3]] + letters[comb[2]] + letters[comb[5]]
            temp_five = letters[comb[0]] + letters[comb[1]] + letters[comb[3]] + letters[comb[5]] + letters[comb[6]]
            temp_six = letters[comb[0]] + letters[comb[1]] + letters[comb[4]] + letters[comb[6]] + letters[comb[5]] + letters[comb[3]]
            temp_seven = letters[comb[0]] + letters[comb[2]] + letters[comb[5]]
            temp_eight = letters[comb[0]] + letters[comb[1]] + letters[comb[2]] + letters[comb[3]] + letters[comb[4]] + letters[comb[5]] + letters[comb[6]]
            temp_nine = letters[comb[0]] + letters[comb[2]] + letters[comb[5]] + letters[comb[6]] + letters[comb[3]] + letters[comb[1]]

            check_numbers = [temp_zero, temp_one, temp_two, temp_three, temp_four, temp_five, temp_six, temp_seven, temp_eight, temp_nine]

            bingo = True
            for check_number in check_numbers:
                if sorted(check_number) not in sorted_input_values:
                    bingo = False
                    break

        if bingo:
            #print("HIIII", check_numbers)
            break

    solution = check_numbers
    sorted_solution = [sorted(string) for string in solution]

    digit = ""
    for value in output_values:
        digit += str((sorted_solution.index(sorted(value))))

    total += int(digit)

print(total)
