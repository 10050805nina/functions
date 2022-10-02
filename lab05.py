
# Treat all the following code as being behind an abstraction layer, you shouldn't need to look at it!

def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return {"name" : name, "lat" : lat, "lon" : lon}
    else:
        return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    if change_abstraction.changed:
        return city["name"]
    else:
        return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    if change_abstraction.changed:
        return city["lat"]
    else:
        return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return city["lon"]
    else:
        return city[2]

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False

### === +++ CITY ABSTRACTION BARRIER +++ === ###


from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    "*** YOUR CODE HERE ***"

def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"


def check_abstraction():
    """
    There's nothing for you to do for this function, it's just here for the extra doctest
    >>> change_abstraction(True)
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    >>> change_abstraction(False)
    """


def make_politician(name, party, age):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> isinstance(woodrow, dict)
    True
    """
    # Make sure you use a dictionary in your implementation!
    "*** YOUR CODE HERE ***"
    

def get_pol_name(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_pol_name(woodrow)
    'Woodrow Wilson'
    >>> lincoln = make_politician('Abraham Lincoln', 'Republican', 52)
    >>> get_pol_name(lincoln)
    'Abraham Lincoln'
    """
    "*** YOUR CODE HERE ***"
    

def get_party(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_party(woodrow)
    'Democrat'
    >>> lincoln = make_politician('Abraham Lincoln', 'Republican', 52)
    >>> get_party(lincoln)
    'Republican'
    """
    "*** YOUR CODE HERE ***"
    

def get_age(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_age(woodrow)
    57
    >>> lincoln = make_politician('Abraham Lincoln', 'Republican', 52)
    >>> get_age(lincoln)
    52
    """
    "*** YOUR CODE HERE ***"
    


