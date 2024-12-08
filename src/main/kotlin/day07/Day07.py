import copy

def has_solution_part1(target, actual, numbers):
    if len(numbers) == 0:
        return target == actual
    if actual > target:
        return 0
    selected = numbers[0]
    new_numbers = copy.deepcopy(numbers[1:])
    return has_solution_part1(target, actual + selected, new_numbers) \
        + has_solution_part1(target, actual * selected, new_numbers) 


def has_solution_part2(target, actual, numbers):
    if len(numbers) == 0:
        return target == actual
    if actual > target:
        return 0
    selected = numbers[0]
    new_numbers = copy.deepcopy(numbers[1:])
    return has_solution_part2(target, actual + selected, new_numbers) \
        + has_solution_part2(target, actual * selected, new_numbers) \
        + has_solution_part2(target, int(str(actual) + str(selected)), new_numbers)
    
part1 = 0
part2 = 0
file = open("./src/main/kotlin/day07/input.txt", "r")

for line in file.readlines():
    line = line.strip().split(": ")
    target = int(line[0])
    numbers = list(map(int, line[1].split(" ")))
    if has_solution_part1(target, 0, numbers):
        part1 += target
    if has_solution_part2(target, 0, numbers):
        part2 += target

print(part1)
print(part2)