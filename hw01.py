"""Homework 1."""

def odd(number):
    """Return whether the number is odd.

    >>> odd(2)
    False
    >>> odd(5)
    True
    """
    if number % 2 == 0:
        return False
    else:
        return True




from math import sqrt

def distance(x1, y1, x2, y2):
    """Calculates the Euclidian distance between two points (x1, y1) and (x2, y2)

    >>> distance(1, 1, 1, 2)
    1.0
    >>> distance(1, 3, 1, 1)
    2.0
    >>> distance(1, 2, 3, 4)
    2.8284271247461903
    """
    return sqrt ((x2-x1)**2+(y2-y1)**2)


def distance3d(x1, y1, z1, x2, y2, z2):
    """Calculates the 3D Euclidian distance between two points (x1, y1, z1) and
    (x2, y2, z2).

    >>> distance3d(1, 1, 1, 1, 2, 1)
    1.0
    >>> distance3d(2, 3, 5, 5, 8, 3)
    6.164414002968976
    """
    return sqrt ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)


from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-5, -1)
    -4
    """
    if b < 0:
        f = a + (-b)
    else:
        f = a + b
    return f # You can replace this line, but don't have to.


from math import sqrt

def quadratic(a, b, c):
    """
    >>> quadratic(1, 0, -1)
    (-1.0, 1.0)
    >>> quadratic(1, 2, 1)
    (-1.0, -1.0)
    >>> quadratic(1, 3, -4)
    (-4.0, 1.0)
    """
    sqrtpart = sqrt(b**2-4*a*c)
    x1 = (-b-sqrtpart)/(2*a)
    x2 = (-b+sqrtpart)/(2*a)
    if x1 > 0:
        return float(x2),float (x1)
    else:
        return float(x1),float (x2)

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0:
        return 1
    elif k <= n:
        product = 1
        counter = 0
        while counter < k:
            product = product * (n-counter)
            counter += 1
        return product 
    else:
        factorial = 1
        if int(n) >= 1:
            for i in range (1,int(n)+1):
                factorial = factorial * i
            return factorial

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    a = 0
    while n > 1:
        print(int(n))
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(n*3+1)
        a += 1
    print(1)
    a=a+1
    return a 

