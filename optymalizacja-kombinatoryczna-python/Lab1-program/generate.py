from random import randrange

if __name__ == '__main__':

    with open("punkty2.txt", "w") as file:
        for _ in range(100):
            file.writelines(f"{randrange(100)}, {randrange(100)}\n")
