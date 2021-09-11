def maximo(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > y and z > x:
        return z
    elif y == x or y == z:
        return y
    elif x == z:
        return x
