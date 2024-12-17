def ex_1(data_file:str) -> int:
    with open(data_file, 'r') as file:
        data = file.read()

    list1 = []
    list2 = []
    distance = 0
    for line in data.split('\n'):
        numbers = line.split('   ')
        list1.append(numbers[0])
        list2.append(numbers[1])

    list1.sort()
    list2.sort()

    for index, number in enumerate(list1):
        distance += abs(int(list1[index])-int(list2[index]))

    return distance
