import boats


def test_compute_number_of_ways_to_win_a_race():
    assert 4 == boats.ways_to_win(time=7, distance=9)

    assert 71503 == boats.ways_to_win(time=71530, distance=940200)


def test_compute_total_score():
    input = [(7, 9), (15, 40), (30, 200)]

    assert 288 == boats.total_score(races=input)
