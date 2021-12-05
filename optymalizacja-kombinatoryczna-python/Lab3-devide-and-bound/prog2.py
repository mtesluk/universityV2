import sys
import csv
import pandas as pd


class Node:
    def __init__(self, value, matrix):
        self.value = value
        self.matrix = matrix

    def get_subnodes(self):
        subs = []
        for i, j in enumerate(self.matrix.columns.values):
            sub_val = self.matrix.values[0][i]
            sub = self.matrix.drop(self.matrix.axes[0].values[0])
            sub = sub.drop(j, axis=1)

            subs.append(Node(self.value + sub_val, sub))
        return subs


def value(node):
    return node.value


def bound(node):
    joint = []
    for row in node.matrix.values:
        joint.append(max(row))

    return sum(joint) + node.value


if __name__ == '__main__':

    try:
        filename = sys.argv[1]
    except IndexError:
        filename = 'dane.csv'

    with open(filename) as read_obj:
        csv_reader = csv.reader(read_obj, skipinitialspace=True)
        dane = [[int(r) for r in row] for row in csv_reader]
    original = pd.DataFrame(dane)

    Q = []
    best = 0
    for i in range(original.shape[1]):
        son_node = original.drop(original.axes[0].values[0])
        son_node = son_node.drop(i, axis=1)
        Q.append(Node(original.values[0][i], son_node))

    while len(Q):
        v = Q.pop()
        for sub_node in v.get_subnodes():
            if value(sub_node) > best:
                best = sub_node.value
            if bound(sub_node) > best:
                Q.append(sub_node)

    print(best)
