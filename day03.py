import re

inp = open("input/day03.txt", "r").read()
print(sum([int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp)]))  # 181345830
inp_filtered = ''.join([re.split(r"don't\(\)", x)[0] for x in re.split(r"do\(\)", inp)])
print(sum([int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp_filtered)]))  # 98729041
