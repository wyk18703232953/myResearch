import random

def main(n: int):
    # 生成测试数据
    # 约定：1 <= a <= b <= n，且需要访问 lst[b]，故列表长度至少为 b+1
    # 为简单起见，令列表长度为 n，b 在 [1, n-1] 范围内
    if n < 2:
        # 规模太小无法满足 b 和 b-1 的索引需求
        print(0)
        return

    a = random.randint(1, n - 1)
    b = random.randint(a, n - 1)  # 保证 a <= b <= n-1

    # 生成 n 个随机整数作为列表
    lst = [random.randint(0, 10**6) for _ in range(n)]

    # 原始逻辑
    lst.sort()
    print(lst[b] - lst[b - 1])


if __name__ == "__main__":
    # 示例：调用 main，规模可以自行修改
    main(10)