import math

def main(n):
    r = 10  # 固定半径，规模由 n 控制
    if n <= 1:
        return 0.0
    t = math.sin(math.pi / n)
    if t == 1:
        return float('inf')
    res = r * t / (1 - t)
    # print(res)
    pass
    return res

if __name__ == "__main__":
    main(1000)