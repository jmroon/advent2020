import re

field_req = {
    'byr': re.compile(r'^(19[2-9][0-9]|200[0-2])$'),
    'iyr': re.compile(r'^(201[0-9]|2020)$'),
    'eyr': re.compile(r'^(202[0-9]|2030)$'),
    'hgt': re.compile(r'^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$'),
    'hcl': re.compile(r'^#[0-9a-f]{6}$'),
    'ecl': re.compile(r'^amb|blu|brn|gry|grn|hzl|oth$'),
    'pid': re.compile(r'^[0-9]{9}$')
}


def part1():
    valid = 0
    with open('./resources/day4_input.txt') as f:
        lines = f.read()
        passports = lines.split("\n\n")
        for passport in passports:
            valid += validate_passport(passport, False)
    print('Part 1 - valid passports:', valid)


def part2():
    valid = 0
    with open('./resources/day4_input.txt') as f:
        lines = f.read()
        passports = lines.split("\n\n")
        for passport in passports:
            valid += validate_passport(passport, True)
    print('Part 2 - valid passports:', valid)


def validate_passport(passport: str, validate_fields: bool) -> bool:
    for field in field_req:
        if field not in passport:
            return False
        elif validate_fields:
            value = passport.split(field + ':')[1].split()[0]
            if not (validate_field(field, value)):
                return False
    return True


def validate_field(field: str, value: str) -> bool:
    return field_req[field].match(value)


if __name__ == "__main__":
    part1()
    part2()
