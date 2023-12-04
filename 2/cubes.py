import dataclasses


@dataclasses.dataclass(frozen=True)
class GameSet:
    red: int = 0
    blue: int = 0
    green: int = 0

    def is_possible(self, ref_set: "GameSet") -> bool:
        return all(
            [
                getattr(self, color) <= getattr(ref_set, color)
                for color in ("red", "blue", "green")
            ]
        )

    def power(self) -> int:
        return self.red * self.green * self.blue


@dataclasses.dataclass(frozen=True)
class Game:
    id: int
    sets: list[GameSet] = dataclasses.field(default_factory=list)

    def is_possible(self, ref_set: GameSet) -> bool:
        return all([set_.is_possible(ref_set) for set_ in self.sets])

    def fewest_set(self) -> GameSet:
        return GameSet(
            **{
                color: max(getattr(set_, color) for set_ in self.sets)
                for color in ("red", "blue", "green")
            }
        )


def parse_game_set(set_: str) -> GameSet:
    return GameSet(
        **{
            color: int(count)
            for count, color in (pair.split() for pair in set_.split(", "))
        }
    )


def parse_game_line(line: str) -> Game:
    id_, sets = line.split(": ")
    return Game(
        id=int(id_.split()[1]),
        sets=[parse_game_set(s) for s in sets.split("; ")],
    )


def parse_file(filename: str) -> list[Game]:
    with open(filename) as f:
        return [parse_game_line(line) for line in f.readlines()]


def process_sum_ids_of_possible_game(filename: str, ref_set: GameSet) -> int:
    games = parse_file(filename)
    return sum(game.id for game in games if game.is_possible(ref_set))


def process_sum_set_powers(filename: str) -> int:
    games = parse_file(filename)
    return sum(g.fewest_set().power() for g in games)
