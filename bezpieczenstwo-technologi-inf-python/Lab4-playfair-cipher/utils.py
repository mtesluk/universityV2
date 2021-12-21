def clear_keyword(keyword):
    new_keyword = ""
    for c in keyword:
        if c not in new_keyword:
            if c == "J":
                new_keyword = new_keyword + "I"
            else:
                new_keyword = new_keyword + c
    return new_keyword


def generate_matrix(keyword):
    matrix = [[0 for i in range(5)] for j in range(5)]
    key_arr = list(clear_keyword(keyword))

    for i in range(65, 91):
        if chr(i) not in key_arr:
            if chr(i) == "J" and "I" not in key_arr:
                key_arr.append("I")
                # is_I_exist = True
            elif chr(i) == "I" or chr(i) == "J" and "I" in key_arr:
                pass
            else:
                key_arr.append(chr(i))

    index = 0
    for i in range(0, 5):
        for j in range(0, 5):
            matrix[i][j] = key_arr[index]
            index += 1

    return matrix


def convert_to_diagraphs(text):
    for s in range(0, len(text) + 1, 2):
        if s < len(text)-1:
            if text[s] == text[s+1]:
                text=text[:s+1]+"X"+text[s+1:]

    if len(text) % 2 != 0:
        text = text[:] + "X"

    return text


def index_locator(char, matrix):
    indexes = []

    if char == "J":
        char = "I"

    for i, j in enumerate(matrix):
        for k, l in enumerate(j):
            if char == l:
                indexes.append(i)
                indexes.append(k)
                return indexes
