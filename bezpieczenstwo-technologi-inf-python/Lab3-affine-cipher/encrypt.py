import sys

k1 = 1
k2 = 0
try:
    k1 = int(sys.argv[1])
    k2 = int(sys.argv[2])
except IndexError:
    pass

calc = lambda x: k1 * x + k2

with open("in.txt") as file:
    input_text = file.read().upper()

output_text = ""
for index, letter in enumerate(input_text):
    if letter == " ":
        encypted_letter = letter
    else:
        letter_index = ord(letter.upper()) - 65
        encypted_letter = chr(calc(letter_index) % 26 + 65)

    output_text += encypted_letter

with open("out.txt", "w") as file:
    file.write(output_text)

