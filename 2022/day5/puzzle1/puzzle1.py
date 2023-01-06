input_file = "day5\puzzle1\input.txt"
# input_file = "day5/puzzle1/test_input.txt"

# stacks = [["N", "Z"], ["D", "C", "M"], ["P"]]
stacks = [["F", "T", "N", "Z", "M", "G", "H", "J"], ["J", "W", "V"], ["H", "T", "B", "J", "L", "V", "G"], ["L", "V", "D", "C", "N", "J", "P", "B"], ["G", "R", "P", "M", "S", "W", "F"], ["M", "V", "N", "B", "F", "C", "H", "G"], ["R", "M", "G", "H", "D"], ["D", "Z", "V", "M", "N", "H"], ["H", "F", "N", "G"]]

with open(input_file, "r") as input_file:
    for line in input_file:
        text_line = line.strip()

        text_line_splitted = text_line.split(" ")

        quantity_to_move = int(text_line_splitted[1])
        from_stack = int(text_line_splitted[3])
        to_stack = int(text_line_splitted[5])

        # print(quantity_to_move, from_stack, to_stack)

        crates_to_move = stacks[from_stack-1][:quantity_to_move]
        # print(crates_to_move)
        stacks[from_stack-1] = stacks[from_stack-1][quantity_to_move:]

        
        stacks[to_stack-1] = crates_to_move[::-1] + stacks[to_stack-1]
        # print(stacks)


crates_on_top = ""

for stack in stacks:
    crates_on_top += stack[0]

print(crates_on_top)