# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
Nove = 9

bin(Nove)                           # 0b1001
Nove.bit_length()                   # 4  # ou (9).bit_loength()
Nove.to_bytes(2, byteorder='big')   # b'\x00\t'