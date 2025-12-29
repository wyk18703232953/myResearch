import random

class ADIYWoodenLadder:
    def solve_case(self, n, a):
        a.sort()
        return min(a[-2] - 1, n - 2)

def main(n):
    solver = ADIYWoodenLadder()

    # 生成测试数据：t 组测试
    # 这里设定 t = max(1, n // 3)，可根据需要调整
    t = max(1, n // 3)

    results = []
    for _ in range(t):
        # 每组数据长度 m，范围 [2, n]
        m = max(2, random.randint(2, n))

        # 生成 m 个台阶高度，范围 [1, n]，可重复
        a = [random.randint(1, n) for _ in range(m)]

        res = solver.solve_case(m, a)
        results.append(res)

    # 输出结果（与原程序行为一致：每组一行）
    for r in results:
        print(r)

if __name__ == "__main__":
    # 示例：调用 main，规模参数可自行调整
    main(10)