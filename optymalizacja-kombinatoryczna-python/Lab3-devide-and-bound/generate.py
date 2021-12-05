from random import randrange
import csv

if __name__ == '__main__':

    num = 15
    with open("dane3.csv", "w", newline='') as file:
        spamwriter = csv.writer(file, delimiter=',')
        for i in range(num):
            spamwriter.writerow(randrange(4294967295) for _ in range(num))
