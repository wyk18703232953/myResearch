from math import sin

def main(n):
    pi = 3.14159265359
    r = n
    if n == 0:
        return
    if n <= 1:
        # print(0.0)
        pass
        return
    denominator = (2 * sin(pi * (1 / 2 - 1 / n))) / (sin(2 * pi / n)) - 1
    if denominator == 0:
        # print(0.0)
        pass
        return
    result = r / denominator
    # print(result)
    pass
if __name__ == "__main__":
    main(10)