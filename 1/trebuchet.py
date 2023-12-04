def parse_file(file_name: str) -> list:
    with open(file_name, "r") as file:
        return [line.strip() for line in file.readlines()]


def process_calibration_value(line: str) -> int:
    digits = [int(char) for char in line if char.isdigit()]
    return int("".join(map(str, (digits[0], digits[-1]))))


def process_calibration_value_upgraded(line: str) -> int:
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    i, first, last = 0, None, None
    while i < len(line):
        if line[i].isdigit():
            first = line[i]
            break
        else:
            for key, value in numbers.items():
                if key in line[: i + 1]:
                    first = value
                    break
            if first:
                break
        i += 1

    i = len(line) - 1
    while i >= 0:
        if line[i].isdigit():
            last = line[i]
            break
        else:
            for key, value in numbers.items():
                if key in line[i:]:
                    last = value
                    break
            if last:
                break
        i -= 1
    return int("".join([first, last]))


def sum_calibration_values(file_name: str) -> int:
    return sum(map(process_calibration_value, parse_file(file_name)))


def sum_calibration_values_upgraded(file_name: str) -> int:
    return sum(map(process_calibration_value_upgraded, parse_file(file_name)))
