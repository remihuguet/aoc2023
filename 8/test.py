import wasteland


def test_parse_file():
    assert wasteland.parse_file("8/example.txt") == (
        "RL",
        [
            wasteland.Node("AAA", l="BBB", r="BBB"),
            wasteland.Node("BBB", l="AAA", r="ZZZ"),
            wasteland.Node("ZZZ", l="ZZZ", r="ZZZ"),
        ],
    )
