#!/usr/bin/python3
import random

def main(n: int):
    # 生成两组测试数据，每组各 n 条 (a, b) 记录
    # 原程序逻辑：先读一组，后读一组，对相同 a 取 b 的最大值，最后求和

    random.seed(0)  # 保持可重复性，如不需要可删除

    ans = {}

    # 第一组 n 条记录
    for _ in range(n):
        a = random.randint(1, 2 * n)
        b = random.randint(1, 1000)
        ans[a] = b

    # 第二组 n 条记录
    for _ in range(n):
        a = random.randint(1, 2 * n)
        b = random.randint(1, 1000)
        if a in ans:
            ans[a] = max(ans[a], b)
        else:
            ans[a] = b

    print(sum(ans.values()))


if __name__ == "__main__":
    # 示例：规模为 10，可根据需要修改或在外部调用 main(n)
    main(10)