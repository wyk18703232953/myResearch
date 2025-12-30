import random

def main(n):
    # 生成测试数据：随机生成 m，范围 [0, 2^n - 1]，避免过大整数
    if n <= 0:
        return
    max_m = (1 << n) - 1
    m = random.randint(0, max_m)

    out = [n]
    i = n - 1
    m -= 1
    for _ in range(n - 1):
        if m % 2:
            out.append(i)
        else:
            out = [i] + out

        m //= 2
        i -= 1

    for v in out:
        print(v, end=" ")
    print()


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)