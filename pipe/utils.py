def partial_fn(fn):
    def wrapper(*args):
        def inner(f):
            return fn(f, *args)
        return inner
    return wrapper


def iff(condition):
    def inner_true(fn):
        def inner_false(gn):
            return fn if condition else gn
        return inner_false
    return inner_true


def mapf(fn):
    def inner(items):
        return [fn(item) for item in items]
    return inner


def filterf(fn):
    def inner(items):
        return [item for item in items if fn(item)]
    return inner


def add(num1):
    def inner(num2):
        return num1 + num2
    return inner


def power(num1):
    def inner(num2):
        return num1 ** num2
    return inner


def sub(num1):
    def inner(num2):
        return num1 - num2
    return inner


def multiply(num1):
    def inner(num2):
        return num1 * num2
    return inner


def divide(num1):
    def inner(num2):
        return num1 / num2
    return inner


def reverse_args(fn):
    def inner_1(arg1):
        def inner_2(arg2):
            return fn(arg2)(arg1)
        return inner_2
    return inner_1
