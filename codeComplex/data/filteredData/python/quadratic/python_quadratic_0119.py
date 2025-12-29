import collections
import random

def main(n: int):
    # 生成测试数据：长度为 n 的数组，元素范围 1..n
    # 可以根据需要调整生成策略
    arr = [random.randint(1, n) for _ in range(n)]

    cs = collections.Counter(arr)
    result = min(cs[x] for x in range(1, n + 1))
    print(result)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)