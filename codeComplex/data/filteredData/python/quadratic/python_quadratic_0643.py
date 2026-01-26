def main(n):
    # 生成确定性输入：长度为 n 的整数数组
    # 这里选择从 1 到 n 的序列，规模和内容完全由 n 决定
    a = list(range(1, n + 1))

    a.sort()
    ans = 0
    u = [0] * (n + 1)
    for i in range(n):
        if u[i] == 0:
            ans += 1
        for j in range(i, n):
            if a[j] % a[i] == 0:
                u[j] = 1
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可按需调整 n 的大小进行时间复杂度实验
    main(10)