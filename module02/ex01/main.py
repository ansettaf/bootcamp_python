class ObjectC(object):
    def __init__(self):
        # placeholder, attributes will be added dynamically
        pass

def what_are_the_vars(*args, **kwargs):
    # if first arg is None -> return None
    if len(args) == 1 and args[0] is None and not kwargs:
        return None
    obj = ObjectC()
    # positional args become var_0, var_1, ...
    for i, val in enumerate(args):
        setattr(obj, f"var_{i}", val)
    # keyword args become attributes as is
    for k, v in kwargs.items():
        setattr(obj, k, v)
    return obj


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
