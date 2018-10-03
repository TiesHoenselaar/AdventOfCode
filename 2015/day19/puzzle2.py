import queue
import re

transitions = {}
fname = 'input.txt'
reading_transitions = True
with open(fname) as f:
    for line in f:
        line = line.strip()

        if not line:
            reading_transitions = False
        elif reading_transitions:
            src, dst = line.split(' => ')
            transitions[dst] = src
        else:
            target = line

def build_iter(input):
    for dst in transitions:
        src = transitions[dst]
        for match in re.finditer(dst, input):
            yield input[:match.start()] + src + input[match.end():]

q = queue.PriorityQueue()
q.put((len(target), 0, target))

while True:
    length, iterations, current = q.get()

    if current == 'e':
        break

    for precursor in build_iter(current):
        q.put((len(precursor), iterations + 1, precursor))

print(iterations)