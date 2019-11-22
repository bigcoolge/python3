def bubble_sort(values):
    if len(values) > 1:
        swap = True
        j = 1
        while swap is True:
            swap = False
            print("===========" + str(j))
            for i in range(len(values) - j):
                if values[i] > values[i+1]:
                    values[i], values[i+1] = values[i+1], values[i]
                    swap = True
            print(values)
            j += 1
    return values


values = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
bubble_sort(values)
