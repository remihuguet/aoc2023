import pytest
import camel


@pytest.fixture
def hands():
    return [
        camel.HandWithoutJ("32T3K", 765),
        camel.HandWithoutJ("T55J5", 684),
        camel.HandWithoutJ("KK677", 28),
        camel.HandWithoutJ("KTJJT", 220),
        camel.HandWithoutJ("QQQJA", 483),
    ]


def test_hands_type(hands):
    assert hands[0].type == "PAIR"
    assert hands[1].type == "THREE"
    assert hands[2].type == "TWOPAIR"
    assert hands[3].type == "TWOPAIR"
    assert hands[4].type == "THREE"
    assert camel.HandWithoutJ("KKKKK", 1).type == "FIVE"
    assert camel.HandWithoutJ("KQKQK", 1).type == "FULL"
    assert camel.HandWithoutJ("KKQKK", 1).type == "FOUR"
    assert camel.HandWithoutJ("23J79", 1).type == "HIGHCARD"


def test_hands_ordering(hands):
    assert hands[0] < hands[1]
    assert hands[2] < hands[4]
    assert hands[2] > hands[3]

    assert sorted(hands) == [hands[0], hands[3], hands[2], hands[1], hands[4]]


def test_total_winning(hands):
    assert camel.total_winning(hands) == 6440


def test_parse_input(hands):
    assert camel.parse("7/example.txt", hand_class=camel.HandWithoutJ) == hands


def test_total_from_input():
    assert (
        camel.total_winning_from("7/example.txt", hand_class=camel.HandWithoutJ) == 6440
    )


def test_best_hands_type():
    hands = [
        camel.HandWithJ("32T3K", 765),
        camel.HandWithJ("T55J5", 684),
        camel.HandWithJ("KK677", 28),
        camel.HandWithJ("KTJJT", 220),
        camel.HandWithJ("QQQJA", 483),
    ]

    assert hands[0].type == "PAIR"
    assert camel.HandWithJ("23J79", 1).type == "PAIR"
    assert camel.HandWithJ("22J8A", 1).type == "THREE"
    assert camel.HandWithJ("22JJA", 1).type == "FOUR"
    assert camel.HandWithJ("22JJJ", 1).type == "FIVE"
    assert camel.HandWithJ("22JAA", 1).type == "FULL"

    assert hands[1].type == "FOUR"
    assert hands[2].type == "TWOPAIR"
    assert hands[3].type == "FOUR"
    assert hands[4].type == "FOUR"
    assert camel.HandWithJ("KKJKK", 1).type == "FIVE"
    assert camel.HandWithJ("KQKQK", 1).type == "FULL"
    assert camel.HandWithJ("KKQKK", 1).type == "FOUR"
    assert camel.HandWithJ("JJJJJ", 1).type == "FIVE"
    assert camel.HandWithJ("QJJQ2", 1).type == "FOUR"


def test_ordering_with_j():
    assert camel.HandWithJ("JKKK2", 1) < camel.HandWithJ("QQQQ2", 1)

    hands = [
        camel.HandWithJ("32T3K", 765),
        camel.HandWithJ("T55J5", 684),
        camel.HandWithJ("KK677", 28),
        camel.HandWithJ("KTJJT", 220),
        camel.HandWithJ("QQQJA", 483),
    ]
    assert sorted(hands) == [hands[0], hands[2], hands[1], hands[4], hands[3]]


def test_total_from_input_with_J():
    assert camel.total_winning_from("7/example.txt", hand_class=camel.HandWithJ) == 5905
