def part1():
    print(slope(3, 1))


def part2():
    print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))


def slope(right, down):
    with open('./resources/day3_input.txt') as f:
        lines = f.readlines()[::down]
        trees = 0
        x = 0
        for line in lines:
            trees += line[x % 31] == "#"
            x += right
    return trees


if __name__ == "__main__":
    part1()
    part2()
