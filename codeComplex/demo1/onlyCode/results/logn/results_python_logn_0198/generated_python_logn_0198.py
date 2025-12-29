def digitsum(x: int) -> int:
    s = 0
    for ch in str(x):
        s += int(ch)
    return s

def main(n: int):
    """
    规模 n 用来生成测试数据：
    - 令 N = 10 ** n（上限数）
    - 令 s = 10 ** (n // 2)（阈值，随规模增长）
    将原程序逻辑应用于 N 和 s。
    """
    N = 10 ** n
    s = 10 ** (n // 2)

    if N - digitsum(N) < s:
        print(0)
        return

    i = 0
    j = N
    while i < j:
        mid = (i + j) // 2
        if mid - digitsum(mid) < s:
            i = mid + 1
        else:
            j = mid

    print(N - i + 1)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 来测试不同规模
    main(3)