from functools import reduce


def ways_to_win(time: int, distance: int) -> int:
    distances = [t * (time - t) for t in range(time + 1)]
    return len([d for d in distances if d > distance])


def total_score(races: list[tuple[int, int]]) -> int:
    scores = [ways_to_win(time=r[0], distance=r[1]) for r in races]
    return reduce(lambda x, y: x * y, scores)
