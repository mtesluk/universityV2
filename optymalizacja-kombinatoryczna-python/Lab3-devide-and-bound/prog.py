import sys
from munkres import Munkres
import csv

if __name__ == '__main__':

    try:
        filename = sys.argv[1]
    except IndexError:
        filename = 'dane.csv'

    with open(filename) as read_obj:
        csv_reader = csv.reader(read_obj, skipinitialspace=True)
        matrix = [[int(r) for r in row] for row in csv_reader]

    cost_matrix = []
    for row in matrix:
        cost_row = []
        for col in row:
            cost_row += [sys.maxsize - col]
        cost_matrix += [cost_row]

    m = Munkres()
    indexes = m.compute(cost_matrix)
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value

    print(total)



