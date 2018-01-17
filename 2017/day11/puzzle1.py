with open("input.txt") as f:
# with open("inputTest.txt") as f:
	content = f.readlines()
content = [x.split(',') for x in content]

directions = content[0]

pos = [0,0,0]
d = 0

for i in range(len(directions)):
        if directions[i] == 'n':
                pos[2] += 1
                pos[1] -= 1
        elif directions[i] == 'ne':
                pos[0] += 1
                pos[1] -= 1
        elif directions[i] == 'se':
                pos[0] += 1
                pos[2] -= 1
        elif directions[i] == 's':
                pos[1] += 1
                pos[2] -= 1
        elif directions[i] == 'sw':
                pos[1] += 1
                pos[0] -= 1
        elif directions[i] == 'nw':
                pos[2] += 1
                pos[0] -= 1
        
        if round((abs(pos[0])+abs(pos[1])+abs(pos[2]))/2) > d:
                d = round((abs(pos[0])+abs(pos[1])+abs(pos[2]))/2)

def get_dist(pos):
        return round((abs(pos[0])+abs(pos[1])+abs(pos[2]))/2)

print(get_dist(pos))
print(d)
                
