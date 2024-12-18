class Guard:
    def __init__(self, map: list):
        self.orientation = 'N'
        self.vector = [-1, 0]
        self.map = map
        self.current_position = self.get_initial_position()

    def get_initial_position(self) -> list:
        for index, row in enumerate(self.map):
            if '^' in row:
                return [index, row.index('^')]

    def get_map(self):
        return self.map

    def get_next_position(self) -> list:
        return [self.current_position[0] + self.vector[0], self.current_position[1] + self.vector[1]]

    def rotate(self):
        if self.orientation == 'N':
            self.orientation = 'E'
            self.vector = [-1, 0]
            return
        elif self.orientation == 'E':
            self.orientation = 'S'
            self.vector = [0, 1]
            return
        elif self.orientation == 'S':
            self.orientation = 'W'
            self.vector = [1, 0]
            return
        elif self.orientation == 'W':
            self.orientation = 'N'
            self.vector = [0, -1]
            return

    def execute_move(self) -> bool:
        next_position = self.get_next_position()
        # Check if the guard leaves the map in the next move
        if next_position[0] == -1 or next_position[0] > len(self.map)-1 or \
                next_position[1] == -1 or next_position[0] > len(self.map[0])-1:
            self.map[self.current_position[0]][self.current_position[1]] = 'X'
            return False
        # Check if a block is in the path
        if self.map[next_position[0]][next_position[1]] == '#':
            self.rotate()
        else:
            # Update map
            self.map[self.current_position[0]][self.current_position[1]] = 'X'
            self.current_position = next_position
        return True

def ex_6(file_path: str) -> int:
    with open(file_path, 'r') as file:
        map = file.read()

    map = map.split('\n')
    formatted_map = [list(row) for row in map]

    guard = Guard(formatted_map)
    # Loop until the guard exits the map
    while guard.execute_move():
        pass

    # Count crosses
    crosses = 0
    for row in guard.map:
        for element in row:
            if 'X' in element:
                crosses += 1
    return crosses