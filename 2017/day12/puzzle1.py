with open("input.txt") as f:
# with open("inputTest.txt") as f:
	content = f.readlines()

	
content = [x.strip() for x in content]

first_nums = []
second_nums = []



for i in range(len(content)):
##for i in range(3):
        pipe = content[i]
        second_num = []
        pipe_splitted = pipe.replace(',','').split(' ')

        first_num = int(pipe_splitted[0])
        for j in range(len(pipe_splitted)-2):
                second_num.append(int(pipe_splitted[j+2]))

        first_nums.append(first_num)
        second_nums.append(second_num)

##print(first_nums)
##print(second_nums)



total_pipes = range(0,len(content))
groups = 0

while len(total_pipes) > 0:
        pipes = [total_pipes[0]]
        for pipe_main in pipes:
                for pipe_sub in second_nums[pipe_main]:
                        if pipe_sub not in pipes:
                                pipes.append(pipe_sub)
        groups += 1
        total_pipes = (list(set(total_pipes)-set(pipes)))

print(groups)
