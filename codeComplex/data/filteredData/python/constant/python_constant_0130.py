import random

def main(n: int):
    """
    n 表示要生成的测试数据数量。
    对每个随机整数 a（范围可根据需要调整），执行原逻辑并打印结果。
    """
    for _ in range(n):
        # 根据 n 生成测试数据：这里生成 [-10^n, 10^n] 范围内的随机整数
        limit = 10 ** max(1, min(n, 9))  # 防止数值过大，这里限制到 10^9
        a = random.randint(-limit, limit)

        # 原始逻辑开始
        if a > 0:
            print(a)
        else:
            a = a - 2 * a  # 相当于 a = -a，取绝对值
            k = a // 10
            b = a % 10
            c = (a // 100) * 10 + b
            if k < c:
                if k != 0:
                    print('-%d' % k)
                else:
                    print(k)
            else:
                if c != 0:
                    print('-%d' % c)
                else:
                    print(c)

if __name__ == "__main__":
    # 示例：生成 5 组测试数据
    main(5)