def get_fib(position):
    if position < 0:
        return -1
    elif position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position - 2) + get_fib(position - 1)


def get_fib2(position):
    if position == 0 or position == 1:
        return position
    return get_fib2(position - 1) + get_fib2(position - 2)


def get_fib3(position, map):
    if position in map:
        return map[position]
    elif position == 0 or position == 1:
        map[position] = position
        return position
    else:
        result = get_fib3(position - 2, map) + get_fib3(position - 1, map)
        map[position] = result
        print(map)
        return result


# Test cases
print(get_fib3(9, {}))
# print get_fib(11)
# print get_fib(0)
