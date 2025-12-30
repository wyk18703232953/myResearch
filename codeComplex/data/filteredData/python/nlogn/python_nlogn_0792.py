import random

def main(n):
    # 生成测试数据
    # 随机生成一个 1 <= k <= n 的值
    k = random.randint(1, n)
    # 生成 n 个随机整数并排序，模拟原代码中的有序 data
    data = sorted(random.randint(0, 1000) for _ in range(n))

    # 原逻辑
    span = data[-1] - data[0]
    delta = [data[i + 1] - data[i] for i in range(n - 1)]
    delta.sort(reverse=True)
    result = span - sum(delta[:k - 1])

    print(result)

# 示例调用
if __name__ == "__main__":
    main(10)