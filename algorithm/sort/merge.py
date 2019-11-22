def merge_sort(values):
    if len(values) <= 1:
        return values
    elif len(values) == 2:
        if values[0] > values[1]:
            values[0], values[1] = values[1], values[0]
        return values
    else:
        pivot = len(values) >> 1
        lHalf = merge_sort(values[:pivot])
        print("====lower half")
        print(lHalf)
        hHalf= merge_sort(values[pivot:])
        print("====higher half")
        print(hHalf)
        return merge(lHalf, hHalf)


def merge(lHalf, hHalf):
    if len(lHalf) == 0:
        return hHalf
    elif len(hHalf) == 0:
        return lHalf
    else:
        if lHalf[0] >= hHalf[len(hHalf) - 1]:
            return hHalf + lHalf
        elif hHalf[0] >= lHalf[len(lHalf) - 1]:
            return lHalf + hHalf
        else:
            values = []
            lHead = 0
            hHead = 0
            while lHead <= (len(lHalf) - 1) and hHead <= (len(hHalf) - 1):
                if lHalf[lHead] <= hHalf[hHead]:
                    values.append(lHalf[lHead])
                    lHead += 1
                else:
                    values.append(hHalf[hHead])
                    hHead += 1
            if lHead <= (len(lHalf) - 1):
                return values + lHalf[lHead:]
            elif hHead <= (len(hHalf) - 1):
                return values + hHalf[hHead:]
            else:
                return values


values = [21, 4, 1, 3, 9, 20, 25]
result = merge_sort(values)
print(result)
