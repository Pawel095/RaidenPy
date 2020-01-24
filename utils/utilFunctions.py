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


def isRemoveable(pos):
    from utils.globals import WIDTH, HEIGHT
    x = False
    y = False
    if pos[0] > 0-100 and pos[0] < WIDTH+100:
        x = True
    if pos[1] > 0-100 and pos[1] < HEIGHT+100:
        y = True
    return x and y
