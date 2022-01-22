import sys
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

keyword = "hello123"
try:
    keyword = sys.argv[1]
except IndexError:
    pass
keyword = keyword.replace(" ", "").upper()

with open("out.txt", "rb") as file:
    input_text = file.read()

des = DES.new(keyword.encode('utf8'), DES.MODE_OFB, b"8bytes12")
res = des.decrypt(input_text)
output_text = unpad(res, DES.block_size)

with open("out_in.txt", "wb") as file:
    file.write(output_text)
