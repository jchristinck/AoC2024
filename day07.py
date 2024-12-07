def f(t, vs, cs, r, part):
    if len(cs) == len(vs):
        return r == t
    if part == 1:
        return (f(t, vs, cs + [vs[len(cs)]], r + vs[len(cs)], part)
                + f(t, vs, cs + [vs[len(cs)]], r * vs[len(cs)], part))
    else:
        return (f(t, vs, cs + [vs[len(cs)]], r + vs[len(cs)], part)
                + f(t, vs, cs + [vs[len(cs)]], r * vs[len(cs)], part)
                + f(t, vs, cs + [vs[len(cs)]], int(str(r) + str(vs[len(cs)])), part))


inp = [list(map(int, line.replace(":", "").split(" "))) for line in open("input/day07.txt", "r").read().splitlines()]
print(sum([line[0] if f(line[0], line[1:], [line[1]], line[1], 1) else 0 for line in inp]))  # 2437272016585
print(sum([line[0] if f(line[0], line[1:], [line[1]], line[1], 2) else 0 for line in inp]))  # 162987117690649

