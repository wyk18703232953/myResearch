def is_prime(x):
    if x < 2:
        return False
    return all(x % i for i in range(2, int(x ** 0.5) + 1))

def core_logic(t):
    for i in range(4, t // 2 + 1):
        if not is_prime(i) and not is_prime(t - i):
            return i, t - i
    return None, None

def main(n):
    if n < 8:
        t = 8

    else:
        t = 2 * n
    a, b = core_logic(t)
    if a is not None:
        # print(a, b)
        pass
if __name__ == "__main__":
    main(100)