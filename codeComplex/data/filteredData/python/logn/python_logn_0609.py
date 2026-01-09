def main(n):
    # 这里根据 n 生成 (n, k)，可按需要修改生成规则
    # 当前示例：k 取 1..n 的中点
    k = n // 2

    start = 0
    cnt = n
    cur = 1

    # 原逻辑：先不断累加 start，直到 start > k
    while start <= k and cnt > 0:
        start += cur
        cnt -= 1
        cur += 1

    ans = 0

    if start != k:
        while cnt > 0:
            if start == k:
                start += cur
                cur += 1
                cnt -= 1
                if cnt <= 0:
                    break
            diff = start - k
            ans += diff
            cnt -= diff
            start = k

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)