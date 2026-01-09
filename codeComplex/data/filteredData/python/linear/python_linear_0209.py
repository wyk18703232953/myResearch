def main(n):
    # 映射含义：
    # n: 代表原程序中的 n（事件数量）
    # s: 固定为 n，用于使规模随 n 增大而增大
    s = n

    # 构造确定性的时间序列 l（原来从输入读取）
    # 使用等差递增，间隔选择为 s+1，使得差值分布合理
    l = [0]
    for i in range(n):
        # 模拟 q,w 输入，构造分钟数 q 和秒数 w
        # 将 i 映射到一个确定性时间点：i*(s+1) 分钟
        # 作为 q，w 固定为 0
        q = i * (s + 1)
        w = 0
        q = q * 60 + w
        l.append(q)

    # 保持原始逻辑
    if l[1] - l[0] > s:
        # print(0, 0)
        pass
        return

    for i in range(n):
        if l[i + 1] - l[i] > 2 * s + 1:
            l[i] += s + 1
            # print(l[i] // 60, l[i] % 60)
            pass
            return

    l[-1] += s + 1
    # print(l[-1] // 60, l[-1] % 60)
    pass
if __name__ == "__main__":
    # 示例规模调用，可根据需要修改 n 的大小进行实验
    main(10)