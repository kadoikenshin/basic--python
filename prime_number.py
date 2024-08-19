a = 61
b = 10

# 61が素数かどうか


def is_prime(a):
    if a <= 1:
        return False
    if a <= 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    i = 5
    while i * i <= a:
        if a % i == 0 or a % (i + 2) == 0:
        return False
        i += 6
        return True


print(f"61 is prime: {is_prime(a)}")


# 10が素数かどうか


def is_prime(b):
    if b <= 1:
        return False
    if b <= 3:
        return True
    if b % 2 == 0 or b % 3 == 0:
        return False
    j = 5
    while j * j <= b:
        if b % j == 0 or b % (j + 2) == 0:
            return False
            j += 6
            return True


print(f"10 is prime: {is_prime(b)}")
