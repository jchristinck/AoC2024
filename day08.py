def antinodes(new_loc):
    if 0 <= new_loc[0] < len(inp) and 0 <= new_loc[1] < len(inp):
        an_simple.add(new_loc)
    while 0 <= new_loc[0] < len(inp) and 0 <= new_loc[1] < len(inp):
        an_full.add(new_loc)
        new_loc = tuple(a - b for a, b in zip(new_loc, diff))


inp = [list(line) for line in open("input/day08.txt", "r").read().splitlines()]
entries = {}
for idy, line in enumerate(inp):
    for idx, el in enumerate(line):
        if el != ".":
            entries.setdefault(el, []).append((idy, idx))
an_simple = set()
an_full = set()
for key in entries:
    for idx, loc in enumerate(entries[key]):
        an_full.add(loc)
        for comp in entries[key][idx + 1:]:
            diff = tuple(a - b for a, b in zip(loc, comp))
            antinodes(tuple(a - b for a, b in zip(comp, diff)))
            diff = tuple(a - b for a, b in zip(comp, loc))
            antinodes(tuple(a - b for a, b in zip(loc, diff)))
print(len(an_simple))  # 336
print(len(an_full))  # 1131
