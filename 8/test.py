import wasteland


def test_parse_file():
    assert wasteland.parse_file("8/example_2.txt") == (
        "LLR",
        {
            "AAA": wasteland.Node("AAA", l="BBB", r="BBB"),
            "BBB": wasteland.Node("BBB", l="AAA", r="ZZZ"),
            "ZZZ": wasteland.Node("ZZZ", l="ZZZ", r="ZZZ"),
        },
    )

    assert wasteland.parse_file("8/example.txt") == (
        "RL",
        {
            "AAA": wasteland.Node("AAA", l="BBB", r="CCC"),
            "BBB": wasteland.Node("BBB", l="DDD", r="EEE"),
            "CCC": wasteland.Node("CCC", l="ZZZ", r="GGG"),
            "DDD": wasteland.Node("DDD", l="DDD", r="DDD"),
            "EEE": wasteland.Node("EEE", l="EEE", r="EEE"),
            "GGG": wasteland.Node("GGG", l="GGG", r="GGG"),
            "ZZZ": wasteland.Node("ZZZ", l="ZZZ", r="ZZZ"),
        },
    )


def test_compute_steps_to_zzz():
    assert wasteland.compute_steps_to_zzz("8/example.txt") == 2
    assert wasteland.compute_steps_to_zzz("8/example_2.txt") == 6


def test_compute_paralell():
    assert wasteland.compute_steps_to_xxz("8/example_3.txt") == 6
