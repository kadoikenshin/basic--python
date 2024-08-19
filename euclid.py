

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        return a


# (1)の最大公約数
print(f"GCD of 10 and 20: {gcd(10, 20)}")

# (2)の最大公約数
print(f"GCD of 14 and 91: {gcd(14, 91)}")

# (3)の最大公約数
print(f"GCD of 91 and 14: {gcd(91, 14)}")
