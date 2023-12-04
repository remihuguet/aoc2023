import engine


def test_parse_file():
    assert [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ] == engine.parse_file("3/example.txt")


def test_find_part_numbers():
    grid = engine.parse_file("3/example.txt")
    part_numbers, _ = engine.find_part_numbers(grid)
    assert part_numbers == [467, 35, 633, 617, 592, 755, 664, 598]


def test_find_sum_parts():
    assert 4361 == engine.compute_sum_parts("3/example.txt")


def test_find_gears():
    assert 467835 == engine.compute_sum_gears("3/example.txt")
