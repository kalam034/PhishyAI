import os
from urllib import parse

from features import url_utils


def get_components(url):
    return parse.urlparse(url)

def get_protocol(url):
    _components = get_components(url)
    return _components.scheme

def get_path_params(url):
    _components = get_components(url)
    return _components.params

def get_path(url):
    """Returns the path as a string."""

    _components = get_components(url)
    return _components.path

def get_file_ext(url):
    path = get_path(url)
    _, extension = os.path.splitext(path)
    return extension[1:] 

def get_domain(url):
    """Returns the domain as a string."""

    _components = get_components(url)
    return _components.netloc

def get_port(url):
    """Returns the port number, if any. Otherwise, returns None.
    Valid port numbers are between 0 and 65535, inclusively.
    """
    _components = get_components(url)
    _port =  _components.port
    return _port if _port != None else -1

def get_fragment(url):
    """Returns the fragment as a string."""
    _components = get_components(url)
    return _components.fragment

def get_query(url):
    """Returns the query as a decoded string."""

    _components = get_components(url)
    return _components.query
def extract_file_ext(url):
  """Returns the URL's file extension, e.g. 'pdf'.

  If there is no file extension, returns an empty string.
  """
  path = get_path(url)
  _, extension = os.path.splitext(path)
  return extension[1:]  # Removes the leading '.' from, e.g., '.txt'.

def get_decoded_query_params(url):
    _query = get_query(url)
    return parse.parse_qs(_query)

def get_encoded_query_params(url):
  """Returns a dict mapping query string variables to encoded values.

  For example, {'id': ['123', '456'], 'login': ['max%40yahoo.com']} could be
  returned.
  """

  _decoded_query_params = get_decoded_query_params(url)
  variables_to_encoded_values = {}

  for variable, values in _decoded_query_params.items():
    encoded_values = [parse.quote(value) for value in values]
    variables_to_encoded_values[variable] = encoded_values
  return variables_to_encoded_values

def get_decoded_query_values(url):
  """Returns a list of string query values without percent-encoding.

  For example, if {'q': ['maple tea'], 'email': ['liz@aol.com']} represents
  the query parameters, then ['maple tea', 'liz@aol.com'] is returned.
  """

  _decoded_query_params = get_decoded_query_params(url)
  values = []
  for _, lists_of_values in _decoded_query_params.items():
    values.extend(lists_of_values)
  return values

def get_encoded_query_values(url):
  """Returns a list of percent-encoded string query values.

  For example, if {'login': ['jay%40hotmail.com'], 'id': ['24', 68']}
  represents the query parameters, then ['jay%40hotmail.com', '24', '68'] is
  returned.
  """

  _encoded_query_params = get_encoded_query_params(url)
  values = []
  for _, lists_of_values in _encoded_query_params.items():
    values.extend(lists_of_values)
  return values

def encodes_characters(url):
  """Returns 1 if the URL encodes characters and 0 otherwise."""
  return int('%' in url)

def uses_https(url):
  """Returns 1 if the URL uses HTTPS and 0 otherwise."""

  protocol = get_protocol(url)
  return int(protocol == 'https')

def uses_default_port_number(url):
  """Returns 1 if the port number is 80 (http) or 443 (https).

  Note that if the URL does not have a port number, then this returns 0.
  """
  _port = get_port(url)
  return int(_port == 80 or _port == 443)

def get_average_query_value_digit_count(decoded_query_values):
  """Returns the average number of digits of query values as a float.

  Digits in the decoded values, e.g. ['$9.99', '3_owls'] are counted.
  """
  return url_utils.get_average_count(
      decoded_query_values, url_utils.get_digit_count)

def get_total_query_value_digit_count(decoded_query_values):
  """Returns the number of digits found in query values as an int.

  Digits in the decoded values, e.g. ['$9.99', '3_owls'] are counted.
  """
  return url_utils.get_total_count(decoded_query_values, url_utils.get_digit_count)

def get_average_query_value_letter_count(decoded_query_values):
  """Returns the average number of letters of query values as a float.

  Letters in the decoded values, e.g. ['a@aol.com', 'a b'], are counted.
  """
  return url_utils.get_average_count(
      decoded_query_values, url_utils.get_letter_count)

def get_total_query_value_letter_count(decoded_query_values):
  """Returns the number of letters found in query values as an int.

  Letters in the decoded values, e.g. ['a@aol.com', 'a b'], are counted.
  """
  return url_utils.get_total_count(
      decoded_query_values, url_utils.get_letter_count)

def get_average_query_value_symbol_count(decoded_query_values):
  """Returns the average number of symbols of query values as a float.

  Symbols are any characters that are not letters, digits, or ASCII special
  characters. Symbols in the decoded values, e.g. ['§ Results', '£45'], are
  counted.
  """
  return url_utils.get_average_count(
      decoded_query_values, url_utils.get_symbol_count)

def get_total_query_value_symbol_count(decoded_query_values):
  """Returns the number of symbols found in query values as an int.

  Symbols are any characters that are not letters, digits, or ASCII special
  characters. Symbols in the decoded values, e.g. ['§ Results', '£45'], are
  counted.
  """
  return url_utils.get_total_count(
      decoded_query_values, url_utils.get_symbol_count)

def get_max_query_value_length(decoded_query_values):
  """Returns the length of the longest query value as an integer.

  The lengths of the decoded values, e.g. ['a@aol.com', 'a b'], are
  considered.
  """
  return url_utils.get_max_length(decoded_query_values)

def get_average_query_value_length(decoded_query_values):
  """Returns the average length of query values as a float."""
  return url_utils.get_average_length(decoded_query_values)

def get_total_query_value_length(decoded_query_values):
  """Returns the total length of the query values as an integer."""
  return url_utils.get_total_length(decoded_query_values)


def get_average_query_variable_digit_count(url):
  """Returns the average number of digits of query variables as a float."""
  _decoded_query_params = get_decoded_query_params(url)
  return url_utils.get_average_count(
      _decoded_query_params.keys(), url_utils.get_digit_count)
  
def get_total_query_variable_digit_count(url):
  """Returns the number of digits in query variables as an integer."""
  _decoded_query_params = get_decoded_query_params(url)
  return url_utils.get_total_count(_decoded_query_params.keys(), url_utils.get_digit_count)

def get_average_query_variable_letter_count(url):
  """Returns the average number of letters of query variables as a float."""
  _decoded_query_params = get_decoded_query_params(url)
  return url_utils.get_average_count(
      _decoded_query_params.keys(), url_utils.get_letter_count)

def get_total_query_variable_letter_count(url):
  """Returns the number of letters in query variables as an integer."""
  _decoded_query_params = get_decoded_query_params(url)
  return url_utils.get_total_count(
      _decoded_query_params.keys(), url_utils.get_letter_count)

def get_average_query_variable_symbol_count(url):
  """Returns the average number of symbols of query variables as a float.

  Symbols are any characters that are not letters, digits, or ASCII special
  characters.
  """
  _decoded_query_params = get_decoded_query_params(url)
  return url_utils.get_average_count(
      _decoded_query_params.keys(), url_utils.get_symbol_count)

def get_total_query_variable_symbol_count(url):
  """Returns the number of symbols of query variables as an integer.

  Symbols are any characters that are not letters, digits, or ASCII special
  characters.
  """
  _decoded_query_params = get_decoded_query_params(url)
  return url_utils.get_total_count(
      _decoded_query_params.keys(), url_utils.get_symbol_count)

def get_max_query_variable_length(url):
  """Returns the length of the longest query variable as an integer."""
  _decoded_query_params = get_decoded_query_params(url)
  return url_utils.get_max_length(_decoded_query_params.keys())

def get_average_query_variable_length(url):
  """Returns the average length of query variables as a float."""
  _decoded_query_params = get_decoded_query_params(url)
  return url_utils.get_average_length(_decoded_query_params.keys())

def get_total_query_variable_length(url):
  """Returns the total length of query variables as an integer."""
  _decoded_query_params = get_decoded_query_params(url)
  return url_utils.get_total_length(_decoded_query_params.keys())

def get_length_ratio(word, url):
  """Returns the ratio of the word's length to the URL's length.

  Args:
    word: A string, e.g. 'www.xe.com'.

  Returns:
    A float for the ratio of the given word to the URL length.
  """
  return len(word) / len(url) if url else 0.0

def is_executable(file_ext):
  """Returns 1 if the extension is 'exe' and 0 otherwise"""
  
  return int(file_ext == 'exe')
