from typing import Any


TYPES = ["FIVE", "FOUR", "FULL", "THREE", "TWOPAIR", "PAIR", "HIGHCARD"]
CARDS_WITHOUT_JOKER = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


class Hand:
    def __init__(self, cards: str, bet: int):
        self.cards = cards
        self.bet = bet

    def __repr__(self) -> str:
        return f"{self.cards}-{self.bet}"

    def __eq__(self, __value: "object") -> bool:
        return (
            isinstance(__value, Hand)
            and self.cards == __value.cards
            and self.bet == __value.bet
        )

    @property
    def counts(self) -> dict[str, int]:
        return {c: self.cards.count(c) for c in self.CARDS_INDEX}

    def __lt__(self, other: "Hand") -> bool:
        if self.type != other.type:
            return TYPES.index(self.type) > TYPES.index(other.type)
        else:
            for i in range(5):
                if self.cards[i] != other.cards[i]:
                    return self.CARDS_INDEX.index(
                        self.cards[i]
                    ) > self.CARDS_INDEX.index(other.cards[i])
        return False


class HandWithJ(Hand):
    CARDS_INDEX = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    @property
    def type(self) -> str:
        if "J" in self.cards:
            j_count = self.cards.count("J")
            if self.raw_type == "HIGHCARD":
                if j_count == 1:
                    return "PAIR"
                if j_count == 2:
                    return "THREE"
                if j_count == 3:
                    return "FOUR"
            if self.raw_type == "PAIR":
                if j_count == 1:
                    return "THREE"
                if j_count == 2:
                    return "FOUR"
            if self.raw_type == "THREE" and j_count == 1:
                return "FOUR"
            if self.raw_type == "TWOPAIR":
                return "FULL"
            return "FIVE"
        return self.raw_type

    @property
    def raw_type(self) -> str:
        return HandWithoutJ(self.cards.replace("J", ""), 1).type


class HandWithoutJ(Hand):
    CARDS_INDEX = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    @property
    def type(self) -> str:
        vals = list(self.counts.values())
        if 5 in vals:
            return "FIVE"
        if 4 in vals:
            return "FOUR"
        if 3 in vals and 2 in vals:
            return "FULL"
        if 3 in vals:
            return "THREE"
        if vals.count(2) == 2:
            return "TWOPAIR"
        if 2 in vals:
            return "PAIR"
        return "HIGHCARD"


def total_winning(hands: list[Hand]) -> int:
    ordered_hands = sorted(hands)
    return sum((i + 1) * h.bet for i, h in enumerate(ordered_hands))


def parse(filename: str, hand_class: type) -> list[Any]:
    with open(filename) as f:
        lines = f.readlines()
        d = [hand_class(line[:5], int(line[5:])) for line in lines]
        return d


def total_winning_from(filename: str, hand_class: type) -> int:
    return total_winning(parse(filename, hand_class))
