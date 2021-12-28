def find_all_no_regex(substring, string, ignore_case = True):
    """ Returns the spans where the substring is in the string.
        Ignore_case is self-explanatory.

        Example:
        find_all_no_regex("abc", "abcdeabc")

        Returns:
        [(0, 3), (5, 8)]
        
    """
    import re
    matches = []
    counter = index = 0
    while True:
        index = string.find(substring)
        if index == -1: break
        matches.append((index + counter, index + counter + len(substring)))
        counter += len(substring)
        index += len(substring)
        string = string[index:]
    return matches


def index_find_regex(pattern, string, ignore_case = True):
    """ Returns the spans of where the pattern is found in
        the string. Ignore_case is self-explanatory.

        Example:
        index_find_regex("abc", "abcdeabc")

        Returns:
        [(0, 3), (5, 8)]
    """
    import re
    if ignore_case:
        pattern = pattern.lower()
        string = string.lower()
    a = list(re.finditer(pattern, string))
    spans = [match.span() for match in a]
    return spans


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
    
def radians_to_degrees(radians):
    from math import pi
    return radians * 180/pi

def degrees_to_radians(degrees):
    from math import pi
    return degrees * pi/180



