def part1():
    with open('../resources/day1_input.txt') as f:
        data = f.read()
    lines = data.splitlines()
    nums = {int(num) for num in lines}
    for num in nums:
        complement = 2020 - num
        if complement in nums:
            return num, complement, num * complement


def part2():
    with open('../resources/day1_input.txt') as f:
        data = f.read()
    lines = data.splitlines()
    nums = {int(num) for num in lines}
    for num in nums:
        remainder = 2020 - num
        for num2 in nums:
            complement = remainder - num2
            if complement in nums:
                return num, num2, complement, num * num2 * complement


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
