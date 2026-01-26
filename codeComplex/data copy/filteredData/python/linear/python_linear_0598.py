from __future__ import division


def main(n):
    out = 0
    for i in range(2, n + 1):
        out += 4 * (n // i - 1) * i
    return out


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次确定性调用
    result = main(10)
    # print(result)
    pass