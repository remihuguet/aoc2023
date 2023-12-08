import seeds


def test_build_map():
    expected = {
        range(50, 50 + 48): range(52, 52 + 48),
        range(98, 98 + 2): range(50, 50 + 2),
    }
    assert seeds.build_map([(50, 98, 2), (52, 50, 48)]) == expected


def test_build_typed_map():
    expected = {
        range(50, 50 + 48): range(52, 52 + 48),
        range(98, 98 + 2): range(50, 50 + 2),
    }
    input = """seed-to-soil map:
50 98 2
52 50 48
"""
    assert seeds.build_typed_map(input) == seeds.Map(
        src="seed", dst="soil", map=expected
    )


def test_parse_file():
    result = seeds.parse_file("5/example.txt")

    assert result.seeds == [79, 14, 55, 13]
    expected = {
        range(50, 50 + 48): range(52, 52 + 48),
        range(98, 98 + 2): range(50, 50 + 2),
    }
    assert seeds.Map(src="seed", dst="soil", map=expected) in result.maps


def test_find_location_for_one_seed():
    plan = seeds.parse_file("5/example.txt")

    assert plan.find("location", 79) == 82


def test_find_min_location():
    assert seeds.find_min_location("5/example.txt") == 35


def test_find_min_location_part_2():
    assert seeds.find_min_location_with_ranges("5/example.txt") == 46
