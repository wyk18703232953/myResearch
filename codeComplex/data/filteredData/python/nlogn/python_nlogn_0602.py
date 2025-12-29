import random

def main(n: int):
    # 1. 生成测试数据
    # 约定：m 为数组 a 的长度，这里设为 n
    m = n

    # 生成一个规模为 m 的整数数组 a
    # 例：元素为 1 到 n 范围内的随机整数
    a = [random.randint(1, n) for _ in range(m)]

    # 2. 原始逻辑
    a.sort()
    same = 0
    p = 1
    for h in a:
        if p <= h:
            p += 1
        else:
            same += 1
    res = a[-1] + same
    ans = sum(a) - res

    # 3. 输出结果（可根据需要也打印生成的数据）
    print(ans)

if __name__ == "__main__":
    # 示例：运行规模 n = 10
    main(10)