def quadrant_calculate(x, y):
    if x > 0 and y > 0:
        return "quadrant I"
    elif x < 0 and y > 0:
        return "quadrant II"
    elif x < 0 and y < 0:
        return "quadrant III"
    elif x > 0 and y < 0:
        return "quadrant IV"
    else:
        return "on an axis"

print(quadrant_calculate(5, 3))   # quadrant I
print(quadrant_calculate(-2, 4))  # quadrant II
print(quadrant_calculate(-3, -3)) # quadrant III
print(quadrant_calculate(4, -1))  # quadrant IV
print(quadrant_calculate(0, 5))