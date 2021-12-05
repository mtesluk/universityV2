import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', help='file', default="punkty.txt")
parser.add_argument('-k', action='store', help='k', default=4)


class Point:
    x = 0
    y = 0
    index = 0

    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"


def distance(p1, p2):
    return math.sqrt(math.pow(p2.x - p1.x, 2) + math.pow(p2.y - p1.y, 2))


def sum_all_points(points):
    n = 0
    for p1 in points:
        for p2 in points:
            if p1.index != p2.index:
                n += distance(p1, p2)
    return n / 2


def sum_with_point(points, point):
    n = 0
    for p4 in points:
        n += distance(p4, point)
    return n


def combine(points, dist_points, new_point):
    # Zamiast ciagle liczyc od nowa kombinacje
    # Usuwam odleglosci ze starym punktem i dodaje z nowym
    max_points = []
    max_dist = 0
    for j in range(len(points)):
        tmp = points[j]
        dist_removed_point = sum_with_point(points, tmp)
        points[j] = new_point
        dist_added_point = sum_with_point(points, new_point)
        dist = dist_points - dist_removed_point + dist_added_point
        if dist > max_dist:
            max_points = points[:]
            max_dist = dist
        points[j] = tmp

    return max_points, max_dist


if __name__ == '__main__':
    args = parser.parse_args()
    filename = args.f
    k = int(args.k)

    P = []
    with open(filename) as file:
        for i, line in enumerate(file.readlines()):
            point = [val.strip() for val in line.split(',')]
            c = Point(int(point[0]), int(point[1]), i)
            P.append(c)

    if 3 > k > len(P):
        print("K za male lub za duze")
        exit()

    if len(P) > 100:
        print("Za duzo elementow wej")
        exit()

    Q = P[:k]
    dist_Q = sum_all_points(Q)
    for p in P[k:]:
        tmp_Q, tmp_dist_Q = combine(Q[:], dist_Q, p)
        if tmp_dist_Q > dist_Q:
            Q = tmp_Q
            dist_Q = tmp_dist_Q

    print(round(dist_Q, 2))
    Q.sort(key=lambda elem: elem.index)
    print(", ".join([str(k.index) for k in Q]))



