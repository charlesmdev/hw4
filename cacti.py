def cacti_number(map):
    count = 0
    row = len(map)
    column = len(map[0])
    def is_valid(x, y):
            return 0 <= x < row and 0 <= y < column and map[x][y] == 0
    for x in range(row):
            for y in range(col):
                if map[x][y] == 0:
                    if (
                        is_valid(x - 1, y) or is_valid(x + 1, y) or
                        is_valid(x, y - 1) or is_valid(x, y + 1)
                    ):
                        count += 1
    return count





