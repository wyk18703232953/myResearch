def f(i):
    return (10 ** i - 10 ** (i - 1)) * i

def main(n):
    i = 1
    total = 0
    # 逻辑与原程序一致，只是将 n 视为规模参数
    while n - f(i) >= 0:
        n -= f(i)
        total += f(i) // i
        i += 1

    # 处理 n % i == 0 的情况，原代码会访问索引 -1
    idx = n % i - 1
    s = str(total + (n + i - 1) // i)
    # 为安全起见，如果索引越界则返回 None 或特殊值
    if not (-len(s) <= idx < len(s)):
        return None
    return s[idx]


if __name__ == "__main__":
    # 示例：用 n=100 作为测试规模，可按需修改或在外部调用 main(n)
    n = 100
    ans = main(n)
    if ans is not None:
        # print(ans)
        pass