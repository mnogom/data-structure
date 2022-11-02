class Pipe:
    def __init__(self):
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
        out = None
        for next in self.__call_stack:
            out = self.__apply_fn(next, out)
        return out

    @property
    def steps(self):
        out = None
        steps = []
        for next in self.__call_stack:
            out = self.__apply_fn(next, out)
            steps.append(out)
        return ' >> '.join(str(step) for step in steps)


if __name__ == '__main__':
    from utils import add, sub, multiply, reverse_args, divide, mapf, filterf


    def is_even(num):
        return num % 2 == 0


    def hey(times):
        return 'hey!' * int(times)


    pipe = Pipe()
    pipe >> 1 >> add(1) >> multiply(2) >> reverse_args(sub)(1) >> reverse_args(divide)(3) >> add(3) >> hey
    print(f'{pipe.result = }')
    # : pipe.result = 'hey!hey!hey!hey!'
    print(f'{pipe.steps = }')
    # : pipe.steps = '1 >> 2 >> 4 >> 3 >> 1.0 >> 4.0 >> hey!hey!hey!hey!'

    pipe = Pipe()
    pipe >> [1, 2, 3] >> mapf(add(1)) >> filterf(is_even) >> len(pipe.result) >> hey

    print(f'{pipe.result = }')
    # : pipe.result = 'hey!hey!'
    print(f'{pipe.steps = }')
    # : pipe.steps = '[1, 2, 3] >> [2, 3, 4] >> [2, 4] >> 2 >> hey!hey!'
