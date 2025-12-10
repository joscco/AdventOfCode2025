import itertools as it
import scipy.optimize as optimize

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def all_combinations(n):
    return it.product([0, 1], repeat=n)

def get_config(config_length, comb, buttons):
    config = [0] * config_length
    for i in range(len(comb)):
        for j in buttons[i]:
            config[j] = (config[j] + comb[i]) % 2
    return config

def find_min_switch_presses(aim, button_list):
    result = float('inf')
    length = len(aim)
    for comb in all_combinations(len(button_list)):
        conf = get_config(length, comb, button_list)
        if conf == aim:
            result = min(length, result, sum(comb))
    return result

def find_min_switch_presses_2(aim, button_mat):
    c = [1] * len(button_mat)
    A_eq = transpose(button_mat)
    b_eq = aim
    return optimize.linprog(c=c, A_eq=A_eq, b_eq=b_eq, integrality=1)


with open("input.txt") as f:
    lines = [line.split() for line in f.read().splitlines()]

    sum_part_1 = 0
    sum_part_2 = 0
    for line in lines:
        aim_config = [['.', '#'].index(x) for x in line[0][1:-1]]
        config_length = len(aim_config)
        button_indices = [[int(x) for x in y[1:-1].split(',')] for y in line[1:-1]]

        min_button_presses = find_min_switch_presses(aim_config, button_indices)
        sum_part_1 += min_button_presses

        aim_joltage = [int(x) for x in line[-1][1:-1].split(',')]
        button_matrix = [[int(i in b) for i in range(config_length)] for b in button_indices]
        min_button_presses_2 = find_min_switch_presses_2(aim_joltage, button_matrix).fun
        sum_part_2 += min_button_presses_2

    print(sum_part_1)
    print(int(sum_part_2))