

def slope(steps_right, steps_down):
    x, y = 0, 0
    count = 0
    while y < len(box):
        if box[y][x] == "#": 
            count += 1
        x += steps_right
        x %= len(box[y])
        y += steps_down
    return count


if __name__ == "__main__":

    with open('input_day3.txt', 'r') as r:
        box = []
        for line in r.readlines():
            box.append(line.strip())

    # part1
    print(slope(3, 1))

    # part2
    result = 1
    for steps_right, steps_down in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        result *= slope(steps_right, steps_down)

    print(result)