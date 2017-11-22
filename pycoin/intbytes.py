"""
Provide the following functions, all cribbed from six http://pythonhosted.org/six/

iterbytes(buf):
    return an iterator of ints corresponding to the bytes of buf

indexbytes(buf, i):
    return the int for the ith byte of buf

int2byte(an_int):
    convert a small integer (< 256) into bytes (with length 1)

byte2int(bs):
    turn bs[0] into an int (0-255)
"""


if bytes == str:
    import functools
    import itertools

    iterbytes = functools.partial(itertools.imap, ord)

    def indexbytes(buf, i):
        return ord(buf[i])
    int2byte = chr

    def byte2int(bs):
        return ord(bs[0])
else:
    import struct

    try:
        import operator

        indexbytes = operator.getitem
        byte2int = operator.itemgetter(0)

    except ImportError:

        # micropython
        indexbytes = lambda buf, i: buf[i]
        byte2int = lambda bs: bs[0]

    iterbytes = iter
    int2byte = struct.Struct(">B").pack
