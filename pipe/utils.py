def partial_fn(fn):
    def wrapper(*args):
        def inner(first_arg):
            def executor():
                return fn(first_arg, *args)

            return executor

        return inner

    return wrapper


def lafn(fn):
    def inner(arg):
        def executor():
            return fn(arg)

        return executor

    return inner


def iff(condition):
    def inner_true(fn):
        def inner_false(gn):
            def executor():
                return fn if condition else gn

            return executor

        return inner_false

    return inner_true


def mapf(fn):
    def inner(items):
        def executor():
            return [fn(item)() for item in items]

        return executor

    return inner


def filterf(fn):
    def inner(items):
        def executor():
            return [item for item in items if fn(item)()]

        return executor

    return inner


def add(num1):
    def inner(num2):
        def executor():
            return num1 + num2

        return executor

    return inner


def power(num1):
    def inner(num2):
        def executor():
            return num1 ** num2

        return executor

    return inner


def sub(num1):
    def inner(num2):
        def executor():
            return num1 - num2

        return executor

    return inner


def multiply(num1):
    def inner(num2):
        def executor():
            return num1 * num2

        return executor

    return inner


def divide(num1):
    def inner(num2):
        def executor():
            return num1 / num2

        return executor

    return inner


def reverse_args(fn):
    def inner_1(arg1):
        def inner_2(arg2):
            return fn(arg2)(arg1)

        return inner_2

    return inner_1


if __name__ == '__main__':
    print(divide(2)(3)())
    print(reverse_args(divide)(2)(3)())
