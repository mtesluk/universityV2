import sys
import utils as u

keyword = "KEYWORD"
try:
    keyword = int(sys.argv[1])
except IndexError:
    pass
keyword = keyword.replace(" ", "").upper()

with open("out.txt") as file:
    input_text = file.read().replace(" ", "").upper()
output_text = ""

matrix = u.generate_matrix(keyword)
diagrams = u.convert_to_diagraphs(input_text)

i = 0
while i < len(diagrams):
    n1 = u.index_locator(diagrams[i], matrix)
    n2 = u.index_locator(diagrams[i + 1], matrix)

    if n1[1] == n2[1]:
        i1 = (n1[0] - 1) % 5
        j1 = n1[1]
        i2 = (n2[0] - 1) % 5
        j2 = n2[1]
        output_text += matrix[i1][j1]
        output_text += matrix[i2][j2]
    elif n1[0] == n2[0]:
        i1 = n1[0]
        j1 = (n1[1] - 1) % 5
        i2 = n2[0]
        j2 = (n2[1] - 1) % 5
        output_text += matrix[i1][j1]
        output_text += matrix[i2][j2]
    else:
        i1 = n1[0]
        j1 = n1[1]
        i2 = n2[0]
        j2 = n2[1]
        output_text += matrix[i1][j2]
        output_text += matrix[i2][j1]

    i += 2

with open("out_in.txt", "w") as file:
    file.write(output_text)
