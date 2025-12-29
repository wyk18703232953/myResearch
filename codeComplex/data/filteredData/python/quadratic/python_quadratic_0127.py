import random

def main(n):
    # 生成测试数据：n 为规模，m 为前缀长度
    # 保证 l 中元素从 1..max_val 范围内随机生成
    max_val = max(1, n)          # 避免 n 为 0
    m = random.randint(0, n)     # 模拟原程序中 m 的取值 (0..n)
    l = [random.randint(1, max_val) for _ in range(n)]

    d = dict()
    if len(set(l)) < n:
        print(0)
        return

    for i in range(m):
        d.setdefault(l[i], 0)
        d[l[i]] += 1

    if not d:
        # 如果 m 为 0，则原逻辑中 d.values() 为空，min 不好取，这里约定输出 0
        print(0)
        return

    min1 = 999999999
    for i in d.values():
        if i < min1:
            min1 = i
    print(min1)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模，可按需修改或在测试框架中调用
    main(10)