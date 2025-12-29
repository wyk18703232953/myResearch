from collections import Counter
import random

def main(n: int):
    # 生成测试数据
    # 为了与原代码语义对应，生成 m 个元素的序列，其中每个元素是 1~n 之间的整数
    # m 的选择：与 n 同级，保证有一定重复
    m = 2 * n
    arr = [str(random.randint(1, n)) for _ in range(m)]

    # 原逻辑开始
    c = Counter(arr).values()
    d = 1
    while sum(ci // d for ci in c) >= n:
        d += 1
    result = d - 1

    # 输出结果
    print(result)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)