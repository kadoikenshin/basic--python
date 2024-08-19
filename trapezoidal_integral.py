from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------


def trapezoidal_inteffration(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
        result *= h
        return result


a = 0
b = math.pi / 2
n = 100

integral_value = trapezoidal_ integration(math.sin, a, b, n)
print(f"The approximate integral of sin(x) from 0 to π/2 is: {integral_value}")
