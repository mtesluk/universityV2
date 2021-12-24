from z3 import *
import re

COLS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def print_net(model):
    net = [[0 for j in range(8)] for i in range(8)]
    matches_fields = re.findall(r"Q_[ABCDEFGH] = [1-8]", str(model))
    for field in matches_fields:
        col = COLS.index(field[2])
        row = 7 - (int(field[-1]) - 1)
        net[row][col] = 1

    for i, l in enumerate(net):
        print(8 - i, end='  ')
        for j, val in enumerate(l):
            print('Q' if val == 1 else '-', end='  ')
        print()
    print(end="   ")
    for i in range(8):
        print(COLS[i], end='  ')


if __name__ == '__main__':
    Q = [Int('Q_%s' % COLS[i]) for i in range(8)]

    # Wartosci pomiedzy 1 i 8
    val_c = [And(1 <= Q[i], Q[i] <= 8) for i in range(8)]

    col_c = [Distinct(Q)]

    diag_c = [If(i == j, True, And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i)) for i in range(8) for j in range(i)]

    s = Solver()
    s.add(val_c)
    s.add(col_c)
    s.add(diag_c)
    if s.check() == sat:
        print_net(s.model())

