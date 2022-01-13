import sys
import utils as u

keyword = "F7AC7D10"
try:
    keyword = sys.argv[1]
except IndexError:
    pass
keyword = keyword.replace(" ", "").upper()

with open("out.txt") as file:
    input_text = file.read().replace(" ", "").upper()
output_text = ""


key = u.hex2int(keyword)
result = u.des(input_text, key, True)
output_text += u.hex2str(u.int2hex(result))


with open("out_in.txt", "w") as file:
    file.write(output_text)
