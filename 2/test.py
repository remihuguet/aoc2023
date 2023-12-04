import cubes


def test_parse_game_line():
    assert cubes.parse_game_line(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    ) == cubes.Game(
        id=3,
        sets=[
            cubes.GameSet(green=8, blue=6, red=20),
            cubes.GameSet(blue=5, red=4, green=13),
            cubes.GameSet(green=5, red=1),
        ],
    )


def test_parse_file():
    assert cubes.parse_file("2/example.txt") == [
        #         Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        cubes.Game(
            id=1,
            sets=[
                cubes.GameSet(blue=3, red=4),
                cubes.GameSet(red=1, green=2, blue=6),
                cubes.GameSet(green=2),
            ],
        ),
        # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        cubes.Game(
            id=2,
            sets=[
                cubes.GameSet(blue=1, green=2),
                cubes.GameSet(green=3, blue=4, red=1),
                cubes.GameSet(green=1, blue=1),
            ],
        ),
        # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        cubes.Game(
            id=3,
            sets=[
                cubes.GameSet(green=8, blue=6, red=20),
                cubes.GameSet(blue=5, red=4, green=13),
                cubes.GameSet(green=5, red=1),
            ],
        ),
        # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        cubes.Game(
            id=4,
            sets=[
                cubes.GameSet(green=1, red=3, blue=6),
                cubes.GameSet(green=3, red=6),
                cubes.GameSet(green=3, blue=15, red=14),
            ],
        ),
        # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        cubes.Game(
            id=5,
            sets=[
                cubes.GameSet(red=6, blue=1, green=3),
                cubes.GameSet(blue=2, red=1, green=2),
            ],
        ),
    ]


def test_game_is_possible():
    ref_set = cubes.GameSet(red=12, green=13, blue=14)
    assert cubes.Game(
        id=5,
        sets=[
            cubes.GameSet(red=6, blue=1, green=3),
            cubes.GameSet(blue=2, red=1, green=2),
        ],
    ).is_possible(ref_set)
    assert not cubes.Game(
        id=3,
        sets=[
            cubes.GameSet(green=8, blue=6, red=20),
            cubes.GameSet(blue=5, red=4, green=13),
            cubes.GameSet(green=5, red=1),
        ],
    ).is_possible(ref_set)


def test_process_sum_ids_of_possible_game():
    assert 8 == cubes.process_sum_ids_of_possible_game(
        "2/example.txt", ref_set=cubes.GameSet(red=12, green=13, blue=14)
    )


def test_game_fewest_set():
    assert (
        cubes.GameSet(red=6, blue=2, green=3)
        == cubes.Game(
            id=5,
            sets=[
                cubes.GameSet(red=6, blue=1, green=3),
                cubes.GameSet(blue=2, red=1, green=2),
            ],
        ).fewest_set()
    )

    assert (
        cubes.GameSet(red=20, blue=6, green=13)
        == cubes.Game(
            id=3,
            sets=[
                cubes.GameSet(green=8, blue=6, red=20),
                cubes.GameSet(blue=5, red=4, green=13),
                cubes.GameSet(green=5, red=1),
            ],
        ).fewest_set()
    )


def test_process_sum_set_powers():
    assert 2286 == cubes.process_sum_set_powers("2/example.txt")
