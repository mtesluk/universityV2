import sys
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


keyword = "hello123"
try:
    keyword = sys.argv[1]
except IndexError:
    pass
keyword = keyword.replace(" ", "").upper()

with open("in.txt") as file:
    input_text = file.read().replace(" ", "").upper()

des = DES.new(keyword.encode('utf8'), DES.MODE_CBC, b"8bytes12")
padded_text = pad(input_text.encode('utf8'), DES.block_size)
output_text = des.encrypt(padded_text)

with open("out.txt", "wb") as file:
    file.write(output_text)
