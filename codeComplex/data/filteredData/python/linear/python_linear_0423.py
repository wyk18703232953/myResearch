def main(n):
    # 构造确定性输入：n, x, a
    if n <= 0:
        return
    x = (n * 3) ^ (n // 2)
    a = [((i * 7) ^ (i // 3) ^ n) & ((1 << 20) - 1) for i in range(n)]

    s = set(a)
    mv = 999  # 保留无用变量以保持结构
    if len(s) < n:
        # print(0)
        pass

    else:
        for i in a:
            if i & x != i and (i & x) in s:
                # print(1)
                pass
                break

        else:
            k = [i & x for i in a]
            if len(set(k)) < n:
                # print(2)
                pass

            else:
                # print(-1)
                pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行复杂度实验
    main(10)