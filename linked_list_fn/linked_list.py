from pair.pair_fn import cons, car, cdr


def make_node(value=None, next=None):
    return cons(value, next)


def get_value(node):
    return car(node)


def get_next(node):
    return cdr(node)


def set_value(node, value):
    return make_node(value, get_next(node))


def set_next(node, next):
    return make_node(get_value(node), next)


def make_linked_list(*values):
    current_value = values[0]
    rest_values = values[1:]
    if len(rest_values) == 0:
        return make_node(current_value)
    return make_node(current_value, make_linked_list(*rest_values))


def to_string(linked_list):
    def inner(node, values=None):
        values = [] if values is None else values
        values = [*values, f'{get_value(node)}']
        if get_next(node) is None:
            return values
        return inner(get_next(node), values)

    return ' > '.join(inner(linked_list))


if __name__ == '__main__':
    ll = make_linked_list(1, 2, 3)
    print(to_string(ll))
