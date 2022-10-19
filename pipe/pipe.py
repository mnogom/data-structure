class Pipe:
    def __init__(self, args=None):
        self.__args = args
        self.__call_stack = []

    def __rshift__(self, next):
        self.__call_stack.append(next)
        return self

    @staticmethod
    def __apply_fn(fn, arg=None):
        if callable(fn):
            return fn(arg)
        return fn

    @property
    def result(self):
        out = self.__args
        for next in self.__call_stack:
            out = self.__apply_fn(next, out)
        return out

    @property
    def steps(self):
        out = self.__args
        steps = []
        for next in self.__call_stack:
            if callable(next):
                out = next(out)
            else:
                out = next
            steps.append(out)
        return ' >> '.join(str(step) for step in steps)


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
        return num2 ** num1
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


def is_even(num):
    return num % 2 == 0


def hey(times):
    return 'hey!' * int(times)


if __name__ == '__main__':
    pipe = Pipe()
    pipe >> 1 >> add(1) >> multiply(2) >> reverse_args(sub)(1) >> reverse_args(divide)(3) >> add(3) >> hey
    print(f'{pipe.result = }')
    print(f'{pipe.steps = }')

    pipe = Pipe()
    pipe >> [1, 2, 3] >> mapf(add(1)) >> filterf(is_even) >> len(pipe.result) >> hey
    print(f'{pipe.result = }')
    print(f'{pipe.steps = }')
