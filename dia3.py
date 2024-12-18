import re


def multiply(mul_statement: str) -> int:
    numbers = re.findall(r'(\d{1,3})', mul_statement)
    return int(numbers[0]) * int(numbers[1])


def ex_3(data_path: str) -> int:
    with open(data_path, 'r') as file:
        data = file.read()

    mult_regex = r'(mul\(\d{1,3},\d{1,3}\))'
    result = 0

    matches = re.findall(mult_regex, data)
    for match in matches:
        result += multiply(match)

    return result
