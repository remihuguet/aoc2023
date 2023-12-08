import dataclasses


def build_map(raw_lines: list[tuple[int, int, int]]) -> dict[int, int]:
    map = {}
    for line in raw_lines:
        dest, src, rg = line
        map[range(src, src + rg)] = range(dest, dest + rg)
    return map


@dataclasses.dataclass(frozen=True)
class Map:
    src: str
    dst: str
    map: dict[int, int] = dataclasses.field(default_factory=dict)


def build_typed_map(raw_input: str) -> Map:
    lines = raw_input.splitlines()
    raw_maps = []
    for line in lines:
        if "map" in line:
            src, _, dst = line.partition(" ")[0].partition("-to-")
        elif line[0].isdigit():
            raw_maps.append(tuple(map(int, line.split(" "))))
    return Map(src=src, dst=dst, map=build_map(raw_maps))


@dataclasses.dataclass
class Plan:
    seeds: list[int]
    maps: list[Map]

    def find(self, dst: str, seed: int) -> int:
        ordered_maps = [
            next(m for m in self.maps if m.dst == "soil"),
            next(m for m in self.maps if m.dst == "fertilizer"),
            next(m for m in self.maps if m.dst == "water"),
            next(m for m in self.maps if m.dst == "light"),
            next(m for m in self.maps if m.dst == "temperature"),
            next(m for m in self.maps if m.dst == "humidity"),
            next(m for m in self.maps if m.dst == "location"),
        ]
        for m in ordered_maps:
            for src_rge, dst_rge in m.map.items():
                if seed in src_rge:
                    seed = dst_rge[seed - src_rge.start]
                    break
        return seed


def parse_file(filename: str) -> Plan:
    with open(filename) as f:
        raw_input = f.read()

        blocks = raw_input.split("\n\n")
        seeds = list(map(int, blocks[0].splitlines()[0].partition(": ")[2].split()))
        maps = list(map(build_typed_map, blocks[1:]))
        return Plan(seeds=seeds, maps=maps)


def find_min_location(filename: str) -> int:
    plan = parse_file(filename)
    return min(plan.find("location", seed) for seed in plan.seeds)


def find_min_location_with_ranges(filename: str) -> int:
    plan = parse_file(filename)
    seeds = []
    for i, seed in enumerate(plan.seeds):
        if i % 2 == 0:
            seeds.extend([r for r in range(seed, seed + plan.seeds[i + 1])])
    print(seeds)
    return min(plan.find("location", seed) for seed in seeds)
