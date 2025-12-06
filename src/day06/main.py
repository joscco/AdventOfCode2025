def to_cephalopod(col):
    new_col = []
    # There are always <= 4 digits in cephalopod numbers
    for i in range(4):
        new_col.append("")
        for col_string in col:
            if i < len(col_string):
                new_col[i] += col_string[i]
    return [int(s) for s in new_col if s.strip() != ""]

def evaluate_columns(operators, columns):
    total = 0
    for op, col_values in zip(operators, columns):
        sub_total = col_values[0]
        for val in col_values[1:]:
            sub_total = sub_total * val if op == "*" else sub_total + val
        total += sub_total
    return total

with open("input.txt") as f:
    cols = []
    operators = []
    raw_lines = f.readlines()

    for x in range(len(raw_lines[-1])):
        ch = raw_lines[-1][x]
        if ch in ["*", "+"]:
            operators.append(ch)
            cols.append([raw_lines[i][x] for i in range(len(raw_lines) - 1)])
        else:
            for i in range(len(raw_lines) - 1):
                cols[-1][i] += raw_lines[i][x]

    int_cols = [[int(col) for col in col_group] for col_group in cols]

    total_part1 = evaluate_columns(operators, int_cols)
    print("Part 1:", total_part1)

    cephalopod_cols = [to_cephalopod(col) for col in cols]
    total_part2 = evaluate_columns(operators, cephalopod_cols)
    print("Part 2:", total_part2)
