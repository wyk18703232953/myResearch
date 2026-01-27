import math

def main(n):
    # Here n is treated as the original input scale for 'n' in the problem.
    # We deterministically generate r based on n.
    original_n = max(2, n)  # ensure valid for angle computation
    r = n + 1

    angle = math.pi / original_n
    c = math.sin(angle)
    k = c / (1 - c)
    R = k * r
    R = float(format(R, '.7f'))
    # print(R)
    pass
if __name__ == "__main__":
    main(10)