import random

def main(n: int):
    # 根据 n 生成测试数据：a 为 1..n 的一个随机排列
    a = list(range(1, n + 1))
    random.shuffle(a)

    # 原逻辑
    if sum(a[i] == i + 1 for i in range(n)) >= n // 1000:
        print("Petr")
    else:
        print("Um_nik")


# 示例：需要时可调用 main(n)
# main(1000000)