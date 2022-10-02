######################
# Required Questions #
######################

# Lambdas

def mul_by_num(num):
    """
    Returns a function that takes one argument and returns num
    times that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    return lambda x : x * num
    


def compose(f, g):
    """Write a function that takes in 2 single-argument functions, f and g, and returns another lambda function 
    that takes in a single argument x. The returned function should return the output of applying f(g(x)). 
    Hint: The staff solution is only 1 line!

    Return the composition function which given x, computes f(g(x)). 

    >>> add_two = lambda x: x + 2  		# adds 2 to x
    >>> square = lambda x: x ** 2 		# squares x
    >>> a = compose(square, add_two) 	# (x + 2 ) ^ 2
    >>> a(5) 
    49
    >>> mul_ten = lambda x: x * 10 		# multiplies 10 with x
    >>> b = compose(mul_ten, a) 		# ((x + 2 ) ^ 2) * 10
    >>> b(5)
    490
    >>> b(2)
    160
    """
    return lambda x : f(g(x)) 
    


def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split()
    d = {word : word_list.count(word) for word in word_list}
    return d
    


def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.
    >>> full_roster = {"bob": "Team A", "barnum": "Team B", "beatrice": "Team C", "bernice": "Team B", "ben": "Team D", "belle": "Team A", "bill": "Team B", "bernie": "Team B", "baxter": "Team A"}
    >>> player_dict = common_players(full_roster)
    >>> dict(sorted(player_dict.items()))
    {'Team A': ['bob', 'belle', 'baxter'], 'Team B': ['barnum', 'bernice', 'bill', 'bernie'], 'Team C': ['beatrice'], 'Team D': ['ben']}
    """
    res = {}
    for i, v in roster.items():
        res[v] = [i] if v not in res.keys() else res[v] + [i]
    return res
    

