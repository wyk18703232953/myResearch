from collections import defaultdict
import random


def main(n: int):
    # 生成测试数据：n 个形如 "(a+b)/c" 的字符串
    # 范围可根据需要调整，这里给出一个简单示例
    expressions = []
    for _ in range(n):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        # 避免除以 0
        c = random.randint(1, 10)
        expressions.append(f"({a}+{b})/{c}")

    dct = defaultdict(int)
    lst = [0.0] * n

    # 按原逻辑解析并统计
    for i in range(n):
        t = expressions[i]
        a, b, c = map(
            int,
            (
                t[1:t.index('+')],
                t[t.index('+') + 1:t.index(')')],
                t[t.index('/') + 1:]
            )
        )
        x = (a + b) / c
        lst[i] = x
        dct[x] += 1

    # 输出结果
    for val in lst:
        print(dct[val], end=' ')


if __name__ == "__main__":
    # 可在此处调整规模 n
    main(10)