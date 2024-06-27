from collections import deque
import dataclasses


@dataclasses.dataclass(frozen=True)
class Node:
    name: str
    l: str
    r: str


def parse_file(filename: str) -> tuple[str, list[Node]]:
    with open(filename) as f:
        lines = f.readlines()
        instructions = lines[0].strip()
        nodes = {}
        for line in lines[2:]:
            name, _, raw_n = line.strip().partition(" = ")
            l, r = (n.strip() for n in raw_n.strip("()").split(","))
            nodes[name] = Node(name, l, r)
    return instructions, nodes


def compute_steps_to_zzz(filename: str) -> int:
    instructions, nodes = parse_file(filename)
    current_node = nodes["AAA"]
    steps = 0
    inst = instructions[0]
    while current_node.name != "ZZZ":
        current_node = nodes[current_node.l] if inst == "L" else nodes[current_node.r]
        steps += 1
        inst = instructions[steps % len(instructions)]
    return steps


def compute_steps_to_xxz(filename: str) -> int:
    instructions, nodes = parse_file(filename)
    starting_nodes = [n for n in nodes.values() if n.name.startswith("A")]
