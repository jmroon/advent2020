def part1():
    with open('./resources/day2_input.txt') as f:
        valid = 0
        data = f.read()
        lines = data.splitlines()
        for line in lines:
            (req, password) = line.split(": ")
            (bounds, char) = req.split()
            (lower, upper) = bounds.split("-")
            valid += int(lower) <= password.count(char) <= int(upper)
        print(valid)


def part2():
    with open('./resources/day2_input.txt') as f:
        valid = 0
        data = f.read()
        lines = data.splitlines()
        for line in lines:
            (req, password) = line.split(": ")
            (bounds, char) = req.split()
            (pos1, pos2) = bounds.split("-")
            match1 = password[int(pos1) - 1] == char
            match2 = password[int(pos2) - 1] == char
            valid += (match1 and not match2) or (not match1 and match2)
        print(valid)


if __name__ == "__main__":
    part1()
    part2()
