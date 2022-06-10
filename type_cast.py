from functools import wraps


def cast(typz):
    def decora(f):
        @wraps(f)
        def newfun(*args):
            return typz(f(*args))
        return newfun
    return decora
