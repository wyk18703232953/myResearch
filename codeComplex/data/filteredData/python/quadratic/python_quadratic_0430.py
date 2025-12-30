import random

def main(n: int):
    # 生成长度为 n 的由 0/1 组成的测试数据字符串
    # 保持和原程序逻辑一致：原来是 list(input()) -> 每个字符再转 int
    a = [random.randint(0, 1) for _ in range(n)]

    smm = 0
    for i in range(n):
        smm += a[i]

    ans = "NO"
    sm = smm
    for div in range(2, n + 1):
        sm = smm
        if not sm % div:
            sm //= div
            f = 0
            s = 0
            for i in range(n):
                s += a[i]
                if s == sm:
                    s = 0
                    f += 1
            if f == div:
                ans = "YES"
                break
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)