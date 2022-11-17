
def multiplication(a, b):
    """
    >>> multiplication(1, 1)
    1
    >>> multiplication(0, 5)
    0
    >>> multiplication(10, 20)
    200
    >>> multiplication(1, 1)
    1
    >>> multiplication(0, 0)
    0
    """
    return a*b

def min_nr(a, b, c):
    """
    >>> min_nr(1, 1, 1)
    1
    >>> min_nr(7, 0, 2)
    0
    >>> min_nr(-1, -1, 2)
    -1
    >>> min_nr(0, 0, 0)
    0
    >>> min_nr(-10, -9, -11)
    -11
    """
    return min(a,b,c)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
