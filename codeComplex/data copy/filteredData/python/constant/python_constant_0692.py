import math

def main(n):
    # 将 n 视为输入规模，同时也作为原程序中的 n
    # r 也从 n 确定性构造：例如 r = n
    if n <= 1:
        # 避免除以零或无意义情况，直接打印 0.0
        # print("0.0000000")
        pass
        return
    r = n
    s = math.sin(math.pi / n)
    result = r * s / (1 - s)
    # print('%.7lf' % result)
    pass
if __name__ == "__main__":
    main(10)