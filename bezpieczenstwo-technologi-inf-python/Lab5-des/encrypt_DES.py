import sys
import utils as u

keyword = "F7AC7D10"
try:
    keyword = sys.argv[1]
except IndexError:
    pass
keyword = keyword.replace(" ", "").upper()

with open("in.txt") as file:
    input_text = file.read().replace(" ", "").upper()
output_text = ""

key = u.hex2int(keyword)
result = u.des(input_text, key)
output_text += u.int2hex(result)


with open("out.txt", "w") as file:
    file.write(output_text)
