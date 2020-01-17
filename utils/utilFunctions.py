def approach(current, target, krok):
    delta = target-current

    return current+delta*krok


def getDist(a, b):
    import math
    return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1]))
