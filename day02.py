import numpy as np


def check_rules(line):
    return (min(line) > -4 and max(line) < 0) or (max(line) < 4 and min(line) > 0)


inp = [[int(x) for x in line.split()] for line in open("input/day02.txt", "r").read().splitlines()]
safe_lists_num = [0, 0]
for line in inp:
    this_report = [line] + [line[:x] + line[x+1:] for x in range(len(line))]
    diffs = [np.diff(opt) for opt in this_report]
    if check_rules(diffs[0]):
        safe_lists_num[0] += 1
    if any([1 for opt in diffs if check_rules(opt)]):
        safe_lists_num[1] += 1
print(safe_lists_num)  # 359, 418
