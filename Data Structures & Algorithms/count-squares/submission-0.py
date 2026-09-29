class CountSquares:
    def __init__(self):
        self.ptcount = defaultdict(int)   # (x, y) -> how many times added
        self.points = []                # list of points, duplicates included

    def add(self, point):
        self.ptcount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point):
        res = 0
        qx, qy = point
        for px, py in self.points:
            if abs(px - qx) != abs(py - qy) or px == qx:
                continue
            res += self.ptcount[(px, qy)] * self.ptcount[(qx, py)]
        return res