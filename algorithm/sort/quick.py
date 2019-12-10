def quick_sort(values):
    start = 0
    end = len(values) - 1
    if end <= start:
        return values
    partition(values, start, end)
    return values


def partition(values, start, end):
    pivot = end
    i = start
    while i < pivot:
        if values[i] > values[pivot]:
            if i == pivot - 1:
                values[i], values[pivot] = values[pivot], values[i]
            else:
                values[i], values[pivot - 1], values[pivot] = values[pivot - 1], values[pivot], values[i]
            pivot -= 1
        else:
            i += 1
    print(pivot)
    print(values)
    print("==============")
    if pivot - 1 > start:
        partition(values, start, pivot - 1)
    if pivot + 1 < end:
        partition(values, pivot + 1, end)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quick_sort(test)