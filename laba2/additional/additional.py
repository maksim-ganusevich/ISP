import builtins
import inspect
from types import FunctionType, CodeType, LambdaType

primitives = (int, str, bool, float,)

def is_iterable(obj):
    return getattr(obj, "__iter__", None) is not None


def is_function(obj):
    return inspect.isfunction(obj) or inspect.ismethod(obj) or isinstance(obj, LambdaType)


def get_global_vars(func):
    globs = {}
    for global_var in func.__code__.co_names:
        if global_var in func.__globals__:
            globs[global_var] = func.__globals__[global_var]
    return globs


def pack_iterable(obj):
    if isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, set):
        packed_iterable = []
        for value in obj:
            if value is None:
                packed_iterable.append(None)
            packed_iterable.append(convert(value))
        if isinstance(obj, tuple):
            return tuple(packed_iterable)
        if isinstance(obj, set):
            return set(packed_iterable)
        return packed_iterable
    elif isinstance(obj, dict):
        packed_dict = {}
        for key, value in obj.items():
            packed_dict[key] = convert(value)
        return packed_dict


def unpack_iterable(obj):
    if isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, set):
        unpacked_iterable = []
        for value in obj:
            if value == None:
                unpacked_iterable.append(None)
            unpacked_iterable.append(deconvert(value))
        if isinstance(obj, tuple):
            return tuple(unpacked_iterable)
        if isinstance(obj, set):
            return set(unpacked_iterable)
        return unpacked_iterable
    elif isinstance(obj, dict):
        unpacked_dict = {}
        for key, value in obj.items():
            unpacked_dict[key] = deconvert(value)
        return unpacked_dict