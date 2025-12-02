def is_silly_number(n: str, max_parts) -> bool:
    for parts in range(2, max_parts + 1):
        if n[:(len(n) // parts)] * parts == n:
            return True
    return False

with open("input.txt") as f:
    sum_a = 0
    sum_b = 0
    for intervall in [line.split("-") for line in f.read().split(",")]:
        for n in range(int(intervall[0]), int(intervall[1]) + 1):
            if is_silly_number(str(n), 2):
                sum_a += n
            if is_silly_number(str(n), len(str(n))):
                sum_b += n
    # Part1
    print(sum_a)
    # Part2
    print(sum_b)
