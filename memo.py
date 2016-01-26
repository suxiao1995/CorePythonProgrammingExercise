import math
__author__ = 'lihui'

def estimate_pi():
    epsilon = 1e-15
    k = 0
    x = math.pi
    while abs(result-x) < epsilon:
        y = (2 * math.sqrt(2)) / 9801
        result = y * (4*k)
