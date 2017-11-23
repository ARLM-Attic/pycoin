
from pycoin.intbytes import iterbytes, byte2int


if hasattr(int, "to_bytes"):
    if not hasattr(int.to_bytes, '__doc__'):
        # micropython has trimed version of int.to/from_bytes without kw args

        def to_bytes(v, length, byteorder="big"):
            return v.to_bytes(length, byteorder)

        def from_bytes(bytes, byteorder="big", signed=False):
            assert signed == False
            return int.from_bytes(bytes, byteorder)

    else:
        # normal python3

        def to_bytes(v, length, byteorder="big"):
            """For python 3, which has a native implementation of this function."""
            return v.to_bytes(length, byteorder=byteorder)


        def from_bytes(bytes, byteorder="big", signed=False):
            """For python 3, which has a native implementation of this function."""
            return int.from_bytes(bytes, byteorder=byteorder, signed=signed)
        
else:
    def to_bytes(v, length, byteorder="big"):
        "See int.to_bytes in python 3"
        l = bytearray()
        for i in range(length):
            mod = v & 0xff
            v >>= 8
            l.append(mod)
        if byteorder == "big":
            l.reverse()
        return bytes(l)

    def from_bytes(bytes, byteorder="big", signed=False):
        "See int.from_bytes in python 3"
        if byteorder != "big":
            bytes = reversed(bytes)
        v = 0
        for c in iterbytes(bytes):
            v <<= 8
            v += c
        if signed and byte2int(bytes) & 0x80:
            v = v - (1 << (8*len(bytes)))
        return v
