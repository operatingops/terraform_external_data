"""
Provides a decorator that implements terraform's external program protocol for data sources.
https://www.terraform.io/docs/providers/external/data_source.html
"""

import json
import sys
from functools import wraps

def error(message):
    """
    Errors must create non-zero status codes and human-readable, ideally one-line, messages on stderr.
    """
    print(message, file=sys.stderr)
    sys.exit(1)


def validate(data):
    """
    Query data and result data must have keys who's values are strings.
    """
    if not isinstance(data, dict):
        error('Data must be a dictionary.')
    for value in data.values():
        if not isinstance(value, str):
            error('Values must be strings.')


def terraform_external_data(function):
    """
    Query data is received on stdin as a JSON object.
    Result data must be returned on stdout as a JSON object.

    The wrapped function must expect its first positional argument to be a dictionary of the query data.
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        query = json.loads(sys.stdin.read())
        validate(query)
        try:
            result = function(query, *args, **kwargs)
        except Exception as e:
            # Terraform wants one-line errors so we catch all exceptions and trim down to just the message (no trace).
            error(f'{type(e).__name__}: {e}')
        validate(result)
        sys.stdout.write(json.dumps(result))
    return wrapper
