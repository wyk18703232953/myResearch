import math

def main(n):
    # Interpret n as the upper bound r, with l fixed at 1
    l = 1
    r = max(1, n)

    a = l
    if a % 2:
        a += 1

    if a + 2 > r:
        result = -1

    else:
        result = (a, a + 1, a + 2)
    return result

if __name__ == "__main__":
    # Example deterministic call
    res = main(10)
    if res == -1:
        # print(-1)
        pass

    else:
        # print(*res)
        pass