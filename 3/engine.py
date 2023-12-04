from collections import defaultdict


def parse_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


def find_part_numbers(grid) -> list[int]:
    parts = []
    gears = []
    gears_candidates = defaultdict(list)
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            is_part = False
            if c.isdigit():
                candidates = []
                if j == 0 or not line[j - 1].isdigit():
                    x = j
                    if line[j - 1] != ".":
                        is_part = True
                        if line[j - 1] == "*":
                            candidates.append((i, j - 1))
                    if i > 0 and j > 0 and grid[i - 1][j - 1] != ".":
                        is_part = True
                        if grid[i - 1][j - 1] == "*":
                            candidates.append((i - 1, j - 1))

                    if i < len(grid) - 1 and j > 0 and grid[i + 1][j - 1] != ".":
                        is_part = True
                        if grid[i + 1][j - 1] == "*":
                            candidates.append((i + 1, j - 1))

                    while x <= len(line) - 1 and line[x].isdigit():
                        if i > 0 and grid[i - 1][x] != ".":
                            is_part = True
                            if grid[i - 1][x] == "*":
                                candidates.append((i - 1, x))

                        if i < len(grid) - 1 and grid[i + 1][x] != ".":
                            is_part = True
                            if grid[i + 1][x] == "*":
                                candidates.append((i + 1, x))

                        x += 1
                    if x <= len(line) - 1 and line[x] != ".":
                        is_part = True
                        if line[x] == "*":
                            candidates.append((i, x))

                    if i > 0 and x <= len(line) - 1 and grid[i - 1][x] != ".":
                        is_part = True
                        if grid[i - 1][x] == "*":
                            candidates.append((i - 1, x))

                    if (
                        i < len(grid) - 1
                        and x <= len(line) - 1
                        and grid[i + 1][x] != "."
                    ):
                        is_part = True
                        if grid[i + 1][x] == "*":
                            candidates.append((i + 1, x))

                    number = int(line[j:x])
                    if is_part:
                        parts.append(number)
                        for cood in candidates:
                            gears_candidates[cood].append(number)
    for cood, numbers in gears_candidates.items():
        if len(numbers) == 2:
            gears.append(numbers[0] * numbers[1])
    return parts, gears


def compute_sum_parts(filename):
    grid = parse_file(filename)
    parts, _ = find_part_numbers(grid)
    return sum(parts)


def compute_sum_gears(filename):
    grid = parse_file(filename)
    _, gears = find_part_numbers(grid)
    return sum(gears)
