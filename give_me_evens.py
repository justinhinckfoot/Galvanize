def get_evens(n, start=0):
    evens = []
    for element in range(start, n):
        if element % 2 == 0:
            evens.append(element)

    return evens

if __name__ == '__main__':

    import sys

    n, start = int(sys.argv[1]), int(sys.argv[2])

    print(get_evens(n, start))
