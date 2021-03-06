def nth_number(n, _list):
    """ If n is a positive integer, find the nth largest distinct number.
        If n is a negative integer, find the nth smallest distinct number.
        n cannot be zero.

        If abs(n) is larger than the number of distinct numbers
        in the list, return the (if n is positive) smallest /
        (if n is negative) largest number in the list.

        Example:
        nth_number(-2, [1,1,2,3,4,5])  # Find the second smallest number

        Returns:
        2
        """

    if type(n) != int: raise TypeError("N must be an integer")
    if n == 0: raise ValueError("Cannot be zero")
    s = set(_list)  # Get rid of duplicates
    l = list(s)
    l.sort()        # Sorted from least to greatest
    if n > 0 and n >= len(l): return l[0]
    elif n > 0 and n < len(l): return l[-n]
    elif n < 0 and -n > len(l): return l[-1]
    elif n < 0 and -n <= len(l): return l[-n-1]


def traverse_list_backwards(list):
    """ Go through a list backwards without reversing it.

        Example:
        for x in traverse_list_backwards([1,2,3]): print(X)

        Returns:
        3
        2
        1
    """
    length = len(list)
    for x in range(-1, -length - 1, -1):
        yield list[x]

def find_all_no_regex(substring, string, ignore_case = True):
    """ Returns the spans where the substring is in the string.
        Ignore_case is self-explanatory.

        Example:
        find_all_no_regex("abc", "abcdeabc")

        Returns:
        [(0, 3), (5, 8)]
    """
    if ignore_case:
        substring = substring.lower()
        string = string.lower()

    matches = []
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1: return matches
        matches.append((start, start + len(substring)))
        start += len(substring) # use start += 1 to find overlapping matches

def find_all_regex(pattern, string, ignore_case = True):
    """ Returns the spans of where the pattern is found in
        the string. Ignore_case is self-explanatory.

        Example:
        find_all_regex("abc", "abcdeabc")

        Returns:
        [(0, 3), (5, 8)]
    """
    if ignore_case:
        pattern = pattern.lower()
        string = string.lower()
    a = list(re.finditer(pattern, string))
    spans = [match.span() for match in a]
    return [string] + spans


def find_pattern_in_file(file, pattern):
    """ Returns a list of regex matches from the named file.

        Example:
        find_pattern_in_file("foo.txt", "[a-zA-Z]+")

        Returns:
        A list of all strings of characters in foo.txt.
    """
    import re
    f = open(file)
    lines = f.read()
    pattern = re.compile(pattern)
    matches = pattern.findall(lines)
    return matches




def add_url_parameters(url, parameters):
    from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
    """ Adds parameters to a url.

        Example:
        url = "http://stackoverflow.com/search?q=question"
        parameters = {'lang':'en','tag':'python'}
        add_url_parameters(url, parameters)

        Returns:
        "http://stackoverflow.com/search?q=question&lang=en&tag=python"
        """
    url_parts = list(urlparse(url))   # Break down old url
    params = parse_qsl(url_parts[4])  # Get old params
    query = dict(params)
    query.update(parameters)          # Put in new params
    url_parts[4] = urlencode(query)   # Make new url
    return urlunparse(url_parts)



def OrderedDict_to_string(dictionary, starttag = "<", delimiter = ", ",
                          endtag = ">", kwstring = False, valstring = False):
    """ Turns an ordereddict to a string. It really can be any dictionary,
        but you should use an ordereddict if you want to keep order in the
        returned string.

        starttag: The start of the string
        delimiter: The string used to seperate each key, value pair
        endtag: The end of the string
        kwstring: If True, all keyword STRINGS (and only strings) will have quotes.
        valstring: If True, all value strings will have quotes.

        Example:
        from collections import OrderedDict
        o = OrderedDict()
        o[1] = "one"
        o["two"] = 2
        OrderedDict_to_string(o)

        Returns:
        <1=one, two=2>
    """

    start = starttag; end = endtag
    for key in dictionary:
        if kwstring: start += repr(key)
        else: start += str(key)
        start += "="

        if valstring: start += repr(str(dictionary[key]))
        else: start += str(dictionary[key])
        start += delimiter

    start = start[:-len(delimiter)]  # Chop off the last delimiter
    start += end
    return start


def radians_to_degrees(radians):
    from math import pi
    return radians * 180/pi

def degrees_to_radians(degrees):
    from math import pi
    return degrees * pi/180


def dec_to_hex(decimal, starttag = "#"):
    """ Convert a decimal to a hex. Starttag will
        precede the result if given. """
    string = hex(decimal)[2:]
    if len(string) < 2: string = "0" + string
    if starttag: return starttag + string
    return string


def rgb_to_hexstring(r, g, b):
    """ Change r,g,b values between 0-255 to a hexstring. """
    red = dec_to_hex(r)
    green = dec_to_hex(g, None)
    blue = dec_to_hex(b, None)
    return red + green + blue

def classExists(classname):
    """ Return True if a class with the given name exists in this namespace. """
    class A: pass
    try:
        if type(eval(classname)) == type (A): return True
        return False
    except: return False

def methodExists(classname, methodname):
    """ Return True if the class has a method named methodname. """
    if classExists(classname):
        if hasattr(eval(classname), methodname) and callable(eval(classname).__dict__[methodname]):
            return True
    return False
