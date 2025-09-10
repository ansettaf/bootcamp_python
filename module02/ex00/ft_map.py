def ft_map(function_to_apply, iterable):
    if not callable(function_to_apply):
        raise TypeError("function_to_apply must be callable")
    try:
        for item in iterable:
            yield function_to_apply(item)
    except TypeError:
        raise TypeError("iterable is not iterable")


def ft_filter(function_to_apply, iterable):
    if function_to_apply is not None and not callable(function_to_apply):
        raise TypeError("function_to_apply must be callable or None")
    try:
        for item in iterable:
            if function_to_apply is None:
                if item:
                    yield item
            else:
                if function_to_apply(item):
                    yield item
    except TypeError:
        raise TypeError("iterable is not iterable")


def ft_reduce(function_to_apply, iterable):
    if not callable(function_to_apply):
        raise TypeError("function_to_apply must be callable")
    it = iter(iterable)
    try:
        accum = next(it)
    except TypeError:
        raise TypeError("iterable is not iterable")
    except StopIteration:
        raise TypeError("reduce() of empty sequence with no initial value")
    for item in it:
        accum = function_to_apply(accum, item)
    return accum
