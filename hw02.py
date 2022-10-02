"""Homework 2."""

def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        count = 1
        while count < n:
            a, b = b, a+b
            count += 1
        return b


def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    filtered = [i for i in lst if i > 0]
    return filtered[0]
        



def has_n(lst, n):
    """ Returns whether or not a list contains the value n.

    >>> has_n([1, 2, 2], 2)
    True
    >>> has_n([0, 1, 2], 3)
    False
    >>> has_n([], 5)
    False
    """
    if lst.count(n) > 0:
        return True
    else:
        return False


def total_price(prices):
    """
    Finds the total price of all products in prices including a
    50% tax on products with a price greater than or equal to 20.
    >>> total_price([5, 20, 30, 7])
    87
    >>> total_price([8, 4, 3])
    15
    >>> total_price([10, 100, 4])
    164
    """
    taxation = []
    for i in prices:
        if i >= 20:
            taxation.append(1.5 * i)
        else:
            taxation.append(i)
    total = int(sum(taxation))
    return total
    


def arange(start, end, step=1):
    """
    arange behaves just like np.arange(start, end, step).
    You only need to support positive values for step.

    >>> arange(1, 3)
    [1, 2]
    >>> arange(0, 25, 2)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    >>> arange(999, 1231, 34)
    [999, 1033, 1067, 1101, 1135, 1169, 1203]

    """
    listlist  = [start]
    term = start
    while start <= term < end: 
        term = term + step
        listlist.append(term)
    return listlist[:len(listlist)-1]
    


def reverse_iter_for(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter_for([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    result = []
    for i in range(len(lst),0,-1):
        result.append(lst[i-1])
    return result

        

def reverse_iter_while(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter_while([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    rev_lst = []
    i = len(lst)
    while 1 <= i <= len(lst):
        rev_lst.append(lst[i-1])
        i -= 1
    return rev_lst
        

