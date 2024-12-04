def is_target_word(word, target_word):
    return word == target_word or word == target_word[::-1]

def part1():
    sum = 0
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix) - 3):
            horiz_word = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] \
                + matrix[row][col + 3]
            if is_target_word(horiz_word, "XMAS"):
                sum += 1

    for row in range(0, len(matrix) - 3):
        for col in range(0, len(matrix)):
            vertical_word = matrix[row][col] + matrix[row + 1][col] + matrix[row + 2][col] \
                + matrix[row + 3][col]
            if is_target_word(vertical_word, "XMAS"):
                sum += 1

    for row in range(0, len(matrix) - 3):
        for col in range(0, len(matrix) - 3):
            main_diagonal = matrix[row][col] + matrix[row + 1][col + 1] + matrix[row + 2][col + 2] \
                + matrix[row + 3][col + 3]
            if is_target_word(main_diagonal, "XMAS"):
                sum += 1

    for row in range(0, len(matrix) - 3):
        for col in range(len(matrix) - 1, 2, -1):
            secondary_diagonal = matrix[row][col] + matrix[row + 1][col - 1] \
                + matrix[row + 2][col - 2] + matrix[row + 3][col - 3]
            if is_target_word(secondary_diagonal, "XMAS"):
                sum += 1
    return sum

def part2():
    sum = 0
    left = []
    right = []

    for row in range(0, len(matrix) - 2):
        for col in range(0, len(matrix) - 2):
            main_diagonal = matrix[row][col] + matrix[row + 1][col + 1] + matrix[row + 2][col + 2]
            if is_target_word(main_diagonal, "MAS"):
                left.append((row +1, col + 1))

    for row in range(0, len(matrix) - 2):
        for col in range(len(matrix) - 1, 1, -1):
            secondary_diagonal = matrix[row][col] + matrix[row + 1][col - 1] \
                + matrix[row + 2][col - 2]
            if is_target_word(secondary_diagonal, "MAS"):
                right.append((row + 1, col - 1))
    return len(list(set(left) & set(right)))

f = open("./src/main/kotlin/day04/input.txt", "r")
matrix = []
for line in f:
    matrix.append(list(line.strip()))
print(part1())
print(part2())