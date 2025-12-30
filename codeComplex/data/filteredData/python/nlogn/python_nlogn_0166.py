def main(n):
    # 1. 生成规模为 n 的测试数据
    #   生成 n 个 (x, w) 对，使得区间 [x-w, x+w] 在一个合理范围内
    #   这里示例：x = 2*i, w = i % 5 + 1（可按需修改生成策略）
    L = []
    for i in range(n):
        x = 2 * i
        w = i % 5 + 1
        L.append([x - w, x + w])

    # 2. 按原逻辑处理（活动选择/区间调度的变形）
    L.sort(reverse=True)
    ans = 0
    edge = 1 << 40
    for i in range(n):
        if L[i][1] <= edge:
            edge = L[i][0]
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用主函数，规模为 10
    main(10)