import util as u
import sys

keyword = "RANDOM"
try:
    keyword = sys.argv[1]
except IndexError:
    pass

with open("out.txt") as file:
    input_text = file.read()

keyword_repeated = u.get_keyword_repeated(keyword, input_text)

output_text = ""
for index, letter in enumerate(input_text):
    if letter == " ":
        encypted_letter = letter
    else:
        keyword_index = ord(keyword_repeated[index]) - 65
        encypted_letter = chr((((ord(letter) - 65) - keyword_index) % 26) + 65)
    output_text += encypted_letter

with open("out_in.txt", "w") as file:
    file.write(output_text)
