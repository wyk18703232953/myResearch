def main(n: int):
    # 依据规模 n 生成测试数据，这里简单设定：
    # l = 0, r = n
    l, r = 0, n

    ans = 0
    if l == r:
        print(0)
        return

    for i in range(63, -1, -1):
        if (r ^ l) & (1 << i):
            for j in range(i, -1, -1):
                ans |= 1 << j
            break
    print(ans)


if __name__ == "__main__":
    # 示例：规模设为 10，可按需要修改
    main(10)