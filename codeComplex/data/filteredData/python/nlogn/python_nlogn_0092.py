import random

def main(n):
    # 生成参数 a, b，满足 1 <= a < n，b 随机
    if n < 2:
        raise ValueError("n 必须至少为 2")
    a = random.randint(1, n - 1)
    b = random.randint(1, n)  # 原代码未使用 b，这里仅保持参数结构

    # 生成测试数据 alist，长度为 n 的随机整数数组
    # 可根据需要调整数值范围
    alist = [random.randint(0, 1000) for _ in range(n)]

    # 按原逻辑执行
    alist.sort(reverse=True)
    p = alist[a - 1]
    q = alist[a]
    print(p - q)

if __name__ == "__main__":
    # 示例：调用 main，n 为规模，可自行修改
    main(10)