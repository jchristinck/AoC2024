print(sum([abs(z[1] - z[0]) for z in zip(*[sorted(y) for y in zip(*[[int(x) for x in line.split()] for line in open("input/day01.txt", "r").read().splitlines()])])]))  # 1941353
print(sum([z * [y for y in zip(*[[int(x) for x in line.split()] for line in open("input/day01.txt", "r").read().splitlines()])][1].count(z) for z in [y for y in zip(*[[int(x) for x in line.split()] for line in open("input/day01.txt", "r").read().splitlines()])][0]]))  # 22539317
