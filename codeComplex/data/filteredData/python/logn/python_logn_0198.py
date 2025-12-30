import random

def digitsum(n: int) -> int:
    s = 0
    for ch in str(n):
        s += int(ch)
    return s

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 原程序读取 n 和 s，这里保留 n 为规模参数，
    # 随机生成一个 0 <= s <= n 的测试值。
    s = random.randint(0, n)

    # 下面是原始逻辑
    if n - digitsum(n) < s:
        print(0)
        return

    i = 0
    j = n
    while i < j:
        mid = (i + j) // 2
        if mid - digitsum(mid) < s:
            i = mid + 1
        else:
            j = mid
    print(n - i + 1)


if __name__ == "__main__":
    # 示例：可以在这里手动指定规模 n
    main(10**6)