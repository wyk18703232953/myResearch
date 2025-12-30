from collections import defaultdict
import random

def main(n):
    # 随机生成测试数据：
    # n 给出树的规模（假设为完全二叉树节点数），我们生成 k 条查询
    # 为保证合法，根位置为 1，叶子在 [1, n] 之间
    # 这里生成 k = n 次查询，起点 cur 随机，操作串长度随机
    k = n
    # 可以固定随机种子以便复现
    random.seed(1)

    # 生成并打印测试输入形式（若想直接使用逻辑，可注释掉这块打印）
    # print(n, k)
    queries = []
    for _ in range(k):
        cur = random.randint(1, n)
        # 操作串长度 1~min(20, n) 个
        m = random.randint(1, min(20, n))
        ops = ''.join(random.choice(['U', 'L', 'R']) for _ in range(m))
        queries.append((cur, ops))
        # print(cur)
        # print(ops)

    # 原逻辑开始
    prev = defaultdict(int)
    for cur, s in queries:
        t = 2
        # 找到比 cur 小的最大 2 的幂 *2（原代码的逻辑）
        while cur % t == 0:
            t *= 2
        t //= 4

        for ch in s:
            if cur == (n + 1) // 2:
                # 在“中点”位置
                if ch == 'U':
                    continue
                else:
                    if ch == 'L':
                        cur -= t
                    else:  # 'R'
                        cur += t
                    t //= 2
            elif cur % 2 == 1:
                # 奇数位置（非中点）
                if ch == "U":
                    if cur & 2 == 0:
                        cur += 1
                    else:
                        cur -= 1
                    t = 1
            else:
                # 偶数位置
                if ch == 'L':
                    cur -= t
                    t //= 2
                elif ch == "U":
                    if cur & (t * 4) == 0:
                        cur += t * 2
                    else:
                        cur -= t * 2
                    t *= 2
                else:  # 'R'
                    cur += t
                    t //= 2
        print(cur)


# 示例运行
if __name__ == "__main__":
    # 可以修改 n 测试不同规模
    main(15)