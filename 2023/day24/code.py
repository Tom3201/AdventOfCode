import sympy

with open("data.txt") as f:
    data = f.read().splitlines()


class Hailstone:
    def __init__(self, sx, sy, sz, vx, vy, vz):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.a = vy
        self.b = -vx
        self.c = vy * sx - vx * sy

    def __repr__(self):
        return "Hailstone{" + f"a={self.a}, b={self.b}, c={self.c}" + "}"


# Part 1
hailstones = [Hailstone(*map(int, line.replace("@", ",").split(","))) for line in data]
total = 0
for i, hailstone1 in enumerate(hailstones):
    for hailstone2 in hailstones[:i]:
        a1, b1, c1 = hailstone1.a, hailstone1.b, hailstone1.c
        a2, b2, c2 = hailstone2.a, hailstone2.b, hailstone2.c
        if a1 * b2 == b1 * a2:
            continue
        x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
        y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
        if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
            if all((x - hs.sx) * hs.vx >= 0 and (y - hs.sy) * hs.vy >= 0 for hs in (hailstone1, hailstone2)):
                total += 1
print(total)

# Part 2
hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in data]
xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")
equations = []
for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 2:
        continue
    total = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
    if len(total) == 1:
        break
print(total[0][xr] + total[0][yr] + total[0][zr])
