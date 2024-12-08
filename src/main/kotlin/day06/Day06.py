def simulate(start, visited, dir_idx): 
    while True:
        next_position = tuple(map(sum, zip(start, directions[dir_idx])))
        if next_position in obstacles:
            dir_idx += 1
            dir_idx %= 4

        start = tuple(map(sum, zip(start, directions[dir_idx])))
        if start[0] not in range(row) or start[1] not in range(row):
            break
        visited.add(start)
    return visited


def next_position(pos, idx):
    # next_pos = tuple(map(sum, zip(pos, directions[idx])))
    next_pos = (pos[0] + directions[idx][0], pos[1] + directions[idx][1])
    while next_pos in obstacles:
        idx += 1
        idx %= 4
        if (next_pos in obstacles):
            # next_pos = tuple(map(sum, zip(pos, directions[idx])))
            next_pos = (pos[0] + directions[idx][0], pos[1] + directions[idx][1])
    return next_pos, idx

def has_cycle(start, visited):
    dir_idx = 0

    # while (start, directions[dir_idx]) not in visited:
    while True:
        if(start,dir_idx) in visited:
            break
        visited.add((start,dir_idx))
        start, dir_idx = next_position(start, dir_idx)

        if start[0] not in range(row) or start[1] not in range(row):
            return False
    return True


def count_cycles(start):
    sum = 0

    for x in range (row):
        for y in range(row):
            obstacles.append((x,y))
            sum += has_cycle(start, set())
            obstacles.remove((x,y))
            # obs_copy = copy.copy(obstacles)
            # obs_copy.append((x, y))
            # sum += has_cycle(start, obs_copy, set())
        print(sum)
    return sum

    

if __name__ == "__main__":
    row = 0
    col = 0
    obstacles = []
    start = ()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    file = open("./src/main/kotlin/day06/input.txt", "r")

    for line in file.readlines():
        col = 0
        for el in line:
            if el == '#':
                obstacles.append((row, col))
            elif el == '^':
                start = (row, col)
            col += 1
        row += 1
    print(len(simulate(start, set(), 0)))
    # Nu merge rahatul asta nu stiu de ce
    print(count_cycles(start))