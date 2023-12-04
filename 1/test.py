import trebuchet


def test_parse_file():
    assert trebuchet.parse_file("1/example.txt") == [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]


def test_process_calibration_value():
    assert trebuchet.process_calibration_value("1abc2") == 12
    assert trebuchet.process_calibration_value("pqr3stu8vwx") == 38
    assert trebuchet.process_calibration_value("treb7uchet") == 77


def test_sum_calibration_values():
    assert trebuchet.sum_calibration_values("1/example.txt") == 142


def test_process_calibration_value_upgraded():
    assert trebuchet.process_calibration_value_upgraded("two1nine") == 29
    assert trebuchet.process_calibration_value_upgraded("eightwothree") == 83
    assert trebuchet.process_calibration_value_upgraded("7pqrstsixteen") == 76


def test_sum_upgraded_calibration_values():
    assert trebuchet.sum_calibration_values_upgraded("1/example_2.txt") == 281
