import scratchcards


def test_compute_card_number():
    assert 4 == scratchcards.compute_card_number(
        winnings=[41, 48, 83, 86, 17], numbers=[83, 86, 6, 31, 17, 9, 48, 53]
    )
    assert 0 == scratchcards.compute_card_number(
        winnings=[87, 83, 26, 28, 32], numbers=[88, 30, 70, 12, 93, 22, 82, 36]
    )
    assert 2 == scratchcards.compute_card_number(
        winnings=[13, 32, 20, 16, 61], numbers=[61, 30, 68, 82, 17, 32, 24, 19]
    )


def test_compute_card_value():
    assert 8 == scratchcards.compute_card_value(
        winnings=[41, 48, 83, 86, 17], numbers=[83, 86, 6, 31, 17, 9, 48, 53]
    )
    assert 0 == scratchcards.compute_card_value(
        winnings=[87, 83, 26, 28, 32], numbers=[88, 30, 70, 12, 93, 22, 82, 36]
    )
    assert 2 == scratchcards.compute_card_value(
        winnings=[13, 32, 20, 16, 61], numbers=[61, 30, 68, 82, 17, 32, 24, 19]
    )


def test_parse_file():
    assert scratchcards.parse_file("4/example.txt") == [
        ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
        ([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
        ([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
        ([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
        ([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
        ([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]),
    ]


def test_compute_total_value():
    assert 13 == scratchcards.compute_total_value("4/example.txt")


def test_compute_total_card_number():
    assert 30 == scratchcards.compute_total_card_number("4/example.txt")
