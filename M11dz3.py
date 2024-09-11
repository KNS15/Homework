import inspect
from pprint import pprint
import sys


def introspection_info(obj):
    result = {'type': type(obj).__name__,
              'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
              'methods': [name for name, value in inspect.getmembers(obj) if callable(value)],
              'module': inspect.getmodule(introspection_info).__name__,
              'getmembers': inspect.getmembers(introspection_info).__ne__}

    return result


number_info = introspection_info(42)
pprint(number_info)
print(sys.platform)
print(sys.version_info)
