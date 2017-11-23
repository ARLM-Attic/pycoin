
try:
    from decimal import Decimal as D

    COIN_PER_SATOSHI = D(1)/SATOSHI_PER_COIN

except ImportError:
    # micropython lacks decimal module, and often, floats.
    def D(n):
        if isinstance(n, int):
            return n
        raise NotImplementedError

    COIN_PER_SATOSHI = NotImplemented

SATOSHI_PER_COIN = D(int(1e8))
SATOSHI_TO_MBTC = D(int(1e5))


def satoshi_to_btc(satoshi_count):
    if satoshi_count == 0:
        return D(0)
    r = satoshi_count * COIN_PER_SATOSHI
    return r.normalize()


def btc_to_satoshi(btc):
    return int(D(btc) * SATOSHI_PER_COIN)


def satoshi_to_mbtc(satoshi_count):
    if satoshi_count == 0:
        return D(0)
    r = satoshi_count / SATOSHI_TO_MBTC
    return r.normalize()


def mbtc_to_satoshi(btc):
    return int(D(btc) * SATOSHI_TO_MBTC)
