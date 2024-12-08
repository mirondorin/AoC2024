from functools import cmp_to_key
key = cmp_to_key(lambda a, b: ((b, a) in edges) - ((a, b) in edges))

f = open("./src/main/kotlin/day05/input.txt", "r")
edges = set()
updates = []
second_section = False
sum = 0

for line in f:
    if line == '\n':
        second_section = True
        continue

    line = line.strip('\n')
    if not second_section:
        parent, child = line.split("|")
        parent = int(parent)
        child = int(child)
        edges.add((parent, child))
    else:
        line = line.split(",")
        updates.append(list(map(int, line)))

for update in updates:
    if update != sorted(update, key = key):
        update = sorted(update, key = key)
        mid = update[len(update) // 2]
        sum += mid

print(sum)