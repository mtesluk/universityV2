import subprocess
import re


def print_net(net):
    for i in net:
        for j in i:
            print(j, end=" ")
        print()


with open("data.lp", 'r') as file:
    text = file.read()

matches_data = re.findall(r"sudoku\([0-9]\,[0-9]\,[0-9]\)", text)

subprocess = subprocess.Popen("clingo data.lp prog.lp", shell=True, stdout=subprocess.PIPE)
out = subprocess.stdout.read().decode("utf-8")

matches_results = re.findall(r"sudoku\([0-9]\,[0-9]\,[0-9]\)", out)

net = [["-" for i in range(9)] for j in range(9) ]

for data in matches_data:
    matches_digits = re.findall(r"[0-9]", data)
    x = int(matches_digits[0])
    y = int(matches_digits[1])
    val = matches_digits[2]

    net[x - 1][y - 1] = val

print("WEJSCIE")
print_net(net)

for data in matches_results:
    matches_digits = re.findall(r"[0-9]", data)
    x = int(matches_digits[0])
    y = int(matches_digits[1])
    val = matches_digits[2]

    net[x - 1][y - 1] = val

print("WYJSCIE")
print_net(net)
