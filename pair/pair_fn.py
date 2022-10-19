from functools import reduce


def cons(car, cdr):
    def inner(message):
        if message == 'car':
            return car
        if message == 'cdr':
            return cdr

    return inner


def car(pair):
    return pair('car')


def cdr(pair):
    return pair('cdr')


if __name__ == '__main__':
    def is_even(num):
        return num % 2 == 0

    def square(num):
        return num ** 2

    pair = cons(2, 10)

