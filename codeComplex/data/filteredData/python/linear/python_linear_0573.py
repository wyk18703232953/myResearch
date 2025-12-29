def main(n: int):
    if n == 1:
        print("1")
    elif n == 2:
        print("1 2")
    else:
        base = 1
        gap = 2
        cur = base
        nxt = 1
        ans = []
        for _ in range(n - 1):
            ans.append(str(base))
            nxt = cur
            cur += gap
            if cur > n:
                base *= 2
                gap *= 2
                cur = base
            nxt = max(nxt, cur)
        ans.append(str(nxt))
        print(" ".join(ans))


# 生成测试数据并调用
if __name__ == "__main__":
    # 示例：根据规模生成一个测试，用户可自行修改 n
    n = 10
    main(n)