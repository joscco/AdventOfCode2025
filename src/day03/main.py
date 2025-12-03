def find_max_joltage(bank: str, digits: int) -> int:
    joltage = ""
    for n in range(digits - 1, -1, -1):
        max_nth_digit = max(set(bank[:len(bank) - n]))
        index = bank.index(max_nth_digit)
        joltage += max_nth_digit
        bank = bank[index + 1:]
    return int(joltage)

with open("input.txt") as f:
    sum_a = 0
    sum_b = 0
    for line in f.readlines():
        sum_a += find_max_joltage(line.strip(), 2)
        sum_b += find_max_joltage(line.strip(), 12)

    print("Part 1:", sum_a)
    print("Part 2:", sum_b)
