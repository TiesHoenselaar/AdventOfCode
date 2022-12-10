input_file = "day4\puzzle1\input.txt"
# input_file = "day4/puzzle1/test_input.txt"

total = 0
with open(input_file, "r") as input_file:
    for line in input_file:
        text_line = line.strip()

        first_range, second_range = text_line.split(",")

        # create list of numbers
        first_list = []
        [start_section, end_section] = [int(x) for x in first_range.split("-")]

        for i in range(start_section, end_section+1):
            first_list.append(i)

        
        # create list of numbers
        second_list = []
        [start_section, end_section] = [int(x) for x in second_range.split("-")]

        for j in range(start_section, end_section+1):
            second_list.append(j)

        check_1 = False
        check_2 = False

        in_the_list = True
        for i in first_list:
            if i not in second_list:
                in_the_list = False
                break
        
        if in_the_list == True:
            check_1 = True

        in_the_list = True
        for j in second_list:
            if j not in first_list:
                in_the_list = False
                break

        if in_the_list == True:
            check_2 = True
        
        if check_1 or check_2:
            total += 1

    print(total)
                
# 246 is too low
# 477 is too high
# 459 is correct