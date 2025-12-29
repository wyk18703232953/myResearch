import random

def solve(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    ba = bin(a)[2:]
    bb = bin(b)[2:]
    r = ''
    if len(ba) != len(bb):
        int('1' * len(bb), 2)
    else:
        for ca, cb in zip(ba, bb):
            if ca == cb:
                r += '0'
            else:
                r += '1'
                break
    r += '1' * (len(bb) - len(r))
    return int(r, 2)


def main(n: int):
    # 生成规模为 n 的测试数据：在 [0, 2^n - 1] 范围内随机生成 a, b
    if n <= 0:
        a = b = 0
    else:
        max_val = (1 << n) - 1
        a = random.randint(0, max_val)
        b = random.randint(0, max_val)
    print(a, b)
    print(solve(a, b))


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)