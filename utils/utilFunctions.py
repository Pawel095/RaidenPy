def approach(current, target, krok):
    delta = target-current

    return current+delta*krok


def getDist(a, b):
    import math
    return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))


def clamp(val, maxv, minv=0):
    ret = val
    if val <= minv:
        ret = minv

    if val >= maxv:
        ret = maxv

    return ret
