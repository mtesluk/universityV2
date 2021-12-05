
from ortools.linear_solver import pywraplp


def main():
    solver = pywraplp.Solver.CreateSolver('GLOP')

    x1 = solver.NumVar(0, 20, 'x1')
    x2 = solver.NumVar(0, 20, 'x2')
    x3 = solver.NumVar(0, 20, 'x3')
    x4 = solver.NumVar(0, 20, 'x4')
    x5 = solver.NumVar(0, 20, 'x5')

    solver.Add(3*x1 + 5*x2 + 2*x3 + 5*x4 + 4*x5 <= 36)
    solver.Add(7*x1 + 12*x2 + 11*x3 + 10*x4 <= 21)
    solver.Add(-3*x2 + 12*x3 + 7*x4 + 2*x5 <= 17)

    solver.Maximize(141*x1 + 393*x2 + 273*x3 + 804*x4 + 175*x5)

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('x1 =', x1.solution_value())
        print('x2 =', x2.solution_value())
        print('x3 =', x3.solution_value())
        print('x4 =', x4.solution_value())
        print('x5 =', x5.solution_value())
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()


