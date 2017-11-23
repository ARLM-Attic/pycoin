
class NoSuchPointError(ValueError):
    pass


class Point:
    """
    A point on an elliptic curve. This a 2-tuple (x, y)
    and also includes a reference to the underlying Curve.
    """

    def __init__(self, x, y, curve):
        self._x, self._y = x, y
        self._curve = curve
        self.check_on_curve()

    def __eq__(self, other):
        return (self._x == other[0]) and (self._y == other[1])

    def __repr__(self):
        return '(%r, %r)' % (self._x, self._y)

    def __getitem__(self, n):
        if n == 0: return self._x
        if n == 1: return self._y
        raise IndexError(n)

    def __iter__(self):
        yield self._x
        yield self._y

    def check_on_curve(self):
        """raise NoSuchPointError (which is a ValueError) if the point is not actually on the curve."""
        if not self._curve.contains_point(*self):
            raise NoSuchPointError('({},{}) is not on the curve {}'.format(self[0], self[1], self._curve))

    def __add__(self, other):
        """Add one point to another point."""
        return self._curve.add(self, other)

    def __sub__(self, other):
        """Subtract one point from another point."""
        return self._curve.add(self, -other)

    def __mul__(self, e):
        """Multiply a point by an integer."""
        return self._curve.multiply(self, e)

    def __rmul__(self, other):
        """Multiply a point by an integer."""
        return self * other

    def __neg__(self):
        """Unary negation"""
        return self.__class__(self[0], self._curve.p()-self[1], self._curve)

    def curve(self):
        """The curve this point is on."""
        return self._curve
