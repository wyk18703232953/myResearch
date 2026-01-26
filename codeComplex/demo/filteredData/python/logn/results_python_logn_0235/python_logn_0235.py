def main(n):
    # 根据 n 自动生成 s（规模参数），这里设为大约 n 的一半
    # 可以按需修改生成规则
    s = n // 2

    if s >= n:
        # print("0")
        pass
        return

    for i in range(s, n + 2):
        cur = 0
        for j in str(i):
            cur += int(j)
        if i - cur >= s:
            break
    # print(n - i + 1)
    pass


# 示例调用（可根据需要修改或删除）
if __name__ == "__main__":
    # 例：n = 100
    main(100)