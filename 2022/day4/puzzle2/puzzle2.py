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

        overlap_found = False
        for i in first_list:
            if overlap_found == False:
                if i in second_list:
                    total += 1
                    overlap_found = True
                    break
                
        for j in second_list:
            if overlap_found == False:
                if j in first_list:
                    total += 1
                    overlap_found = True
                    break
                

    print(total)