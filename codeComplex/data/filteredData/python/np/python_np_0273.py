def maxx(n):
    return n & -n

def main(n):
    """
    根据规模 n 自动生成测试数据并执行原逻辑。
    测试数据设计：
      - q = n（生成 n 个查询）
      - 初始位置 x 初始为中点 root，每个查询从 root 开始
      - 每个查询的指令串 s 为在高度 ~log2(n) 内随机在 'U', 'L', 'R' 中选择，
        这里为了确定性和不依赖随机数，使用固定模式生成。
    """
    # 根节点
    root = n // 2 + 1

    # 生成 q（查询次数）
    q = n  # 可按需调整为其他函数，如 q = max(1, n // 2)

    # 为确定性起见，不使用随机，构造有规律的指令串
    # 指令长度设为与树高度同阶：~log2(n)
    import math
    if n <= 1:
        height = 1
    else:
        height = int(math.log2(n)) + 1

    # 构造 q 个查询
    for qi in range(q):
        # 每个查询从 root 开始
        x = root

        # 指令串模式：循环使用 "ULR" 的前 height 个字符
        pattern = "ULR"
        s = ''.join(pattern[(qi + i) % 3] for i in range(height))

        # 原逻辑
        for ch in s:
            if ch == 'U' and x != root:
                p = x + maxx(x)
                if x == p - maxx(p) // 2:
                    x = p
                else:
                    x = x - maxx(x)
            elif ch == 'L':
                x = x - maxx(x) // 2
            elif ch == 'R':
                x = x + maxx(x) // 2

        print(x)


if __name__ == "__main__":
    # 可在此处指定规模 n，用于本地运行测试
    # 例如：
    main(10)