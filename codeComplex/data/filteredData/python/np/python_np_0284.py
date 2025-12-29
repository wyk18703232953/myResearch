#   ==========     //\\       //||     ||====//||
#       ||        //  \\        ||     ||   // ||
#       ||       //====\\       ||     ||  //  ||
#       ||      //      \\      ||     || //   ||
#   ========== //        \\  ========  ||//====|| 
#  code

def main(n):
    """
    将原交互式程序改为参数化版本：
    - n: 规模（原代码中的 n）
    - 自动生成测试数据并执行同样的逻辑
    """

    # ====== 测试数据生成策略 ======
    # 令查询数 q 与 n 同阶，这里取 q = min(n, 10) 避免规模过大
    q = min(n, 10)

    # 为每个查询生成：
    #   node: 取范围 [1, n] 内的某个节点（这里简单均匀取）
    #   s: 操作序列，由 'L', 'R', 'U' 组成，长度与 log2(n) 同阶
    #       取 len_s = max(1, int(log2(n)))，并做一个固定模式便于复现
    import math
    len_s = max(1, int(math.log2(max(n, 2))))

    # 固定操作模式，保证可重复：例如 "LRU" 循环
    pattern = "LRU"
    queries = []
    for idx in range(q):
        # 均匀选取节点：避免越界
        node = 1 + (idx * max(1, n // q)) % n
        # 生成长度为 len_s 的操作串
        s = "".join(pattern[i % len(pattern)] for i in range(len_s))
        queries.append((node, s))

    # ====== 原逻辑执行 ======
    results = []
    for node, s in queries:
        for ch in s:
            if ch == 'L':
                if node % 2:
                    continue
                k = node & (-node)
                node -= k
                k //= 2
                node += k

            if ch == 'R':
                if node % 2:
                    continue
                k = node & (-node)
                k //= 2
                node += k

            if ch == 'U':
                if node == (n + 1) // 2:
                    continue
                k = node & (-node)
                node -= k
                k *= 2
                node |= k
        results.append(node)

    # 输出结果（保持与原程序行为一致：逐行输出最终 node）
    for ans in results:
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(16)
    main(16)