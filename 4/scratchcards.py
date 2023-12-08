from collections import defaultdict


def compute_card_value(winnings: list[int], numbers: list[int]) -> int:
    power = compute_card_number(winnings, numbers)
    return 2 ** (power - 1) if power > 0 else 0


def compute_card_number(winnings: list[int], numbers: list[int]) -> int:
    return len(set(winnings).intersection(set(numbers)))


def parse_file(filename: str) -> list[tuple[list[int], list[int]]]:
    with open(filename) as file:
        res = []
        for line in file.readlines():
            _, numbers = line.split(":")
            winnings = list(map(int, numbers.split("|")[0].split()))
            nums = list(map(int, numbers.split("|")[1].split()))
            res.append((winnings, nums))
    return res


def compute_total_value(filename: str) -> int:
    return sum(
        [
            compute_card_value(winnings, numbers)
            for winnings, numbers in parse_file(filename)
        ]
    )


def compute_total_card_number(filename: str) -> int:
    raw_cards = parse_file(filename)
    cards = {k: 1 for k in range(1, len(raw_cards) + 2)}

    for i, (w, n) in enumerate(raw_cards):
        card_number = compute_card_number(w, n)
        for j in range(i + 2, i + 2 + card_number):
            cards[j] += cards[i + 1]
    return sum(val for k, val in cards.items() if k < len(raw_cards) + 1)
