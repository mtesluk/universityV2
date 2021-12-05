from random import randrange
import json

if __name__ == '__main__':

    l = [randrange(100) for _ in range(25)]
    with open("dane2.json", "w", newline='') as file:
        json.dump(l, file)
