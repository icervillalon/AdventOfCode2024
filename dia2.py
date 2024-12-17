def validate_report(report: list) -> bool:
    print(report)
    flag_increasing = True
    # Check if first values are increasing or decreasing
    if int(report[0]) > int(report[1]):
        flag_increasing = False
    for index, number in enumerate(report):
        if index != len(report)-1:
            increasing_check = True
            if int(number) > int(report[index + 1]):
                increasing_check = False
            if flag_increasing != increasing_check:
                return False

            if 1 <= abs(int(number) - int(report[index + 1])) <= 3:
                continue
            else:
                return False
        return True


def ex_2(data_path: str) -> int:
    with open(data_path, 'r') as file:
        data = file.read()

    reports_ok = 0
    for line in data.split('\n'):
        report = line.split(' ')
        if validate_report(report):
            reports_ok += 1
    return reports_ok