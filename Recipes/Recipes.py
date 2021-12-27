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



