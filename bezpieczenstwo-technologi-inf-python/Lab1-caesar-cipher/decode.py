import sys

letters = 'aąbcćdeęfghijklłmnoópqrsśtuvwxyzźżAĄBCĆDEĘFGHIJKLŁMNOÓPRSŚTUVWXYZŹŻ'

shift = 0
try:
    shift = int(sys.argv[1])
except IndexError:
    pass

with open("out.txt") as file:
    input_text = file.read()

output_text = ""

for k in input_text:
    i = letters.find(k)

    if i != -1:
        output_text += letters[(i - shift) % len(letters)]
    else:
        output_text += k

with open("out_in.txt", "w") as file:
    file.write(output_text)
