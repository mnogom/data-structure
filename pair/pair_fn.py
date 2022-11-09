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
