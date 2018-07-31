"""
Reference:
    https://www3.nd.edu/~zxu2/acms40390F15/Lec-4.1.pdf
    https://www.math.ust.hk/~mamu/courses/231/Slides/CH04_1B.pdf
"""

import math

"""
1st derivative approximation (obtained by Lagrange interpolation)
"""

def diff_3points(points, position):
    if position == 'start':
        return (-3 * points[0][1] + 4 * points[1][1] - points[2][1]) / (points[2][0] - points[0][0])
    elif position == 'middle':
        return (-points[0][1] + points[2][1]) / (points[2][0] - points[0][0])
    elif position == 'end':
        return (points[0][1] - 4 * points[1][1] + 3 * points[2][1]) / (points[2][0] - points[0][0])
    else:
        return "error"

def diff_5points(points, position):
    summation = 0.0
    for i in range(len(points)-1):
        summation += points[i+1][0] - points[i][0]
    h = summation / (len(points)-1)   
    if position == 'start':
        return (-25 * points[0][1] + 48 * points[1][1] - 36 * points[2][1] + 16 * points[3][1] - 3 * points[4][1]) / (12*h)
    elif position == 'middle':
        return (points[0][1] - 8 * points[1][1] + 8 * points[3][1] - points[4][1]) / (12*h)
    elif position == 'end':
        return (3 * points[0][1] - 16 * points[1][1] + 36 * points[2][1] - 48 * points[3][1] + 25 * points[4][1]) / (12*h)
    else:
        return "error"

"""
2nd derivative approximation (obtained by Taylor polynomial)
"""
def diff2_3points(points, position):
    summation = 0.0
    for i in range(len(points)-1):
        summation += points[i+1][0] - points[i][0]
    h = summation / (len(points)-1)
    if position == 'middle':
        return (points[0][1] - 2*points[1][1] + points[2][1]) / (h*h)
    else:
        return "error"
