import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里示例为生成 n 组 (x, y, z, t1, t2, t3) 并逐组判断
    results = []
    for _ in range(n):
        # 可按需调整数据范围
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        z = random.randint(-10**6, 10**6)
        t1 = random.randint(1, 10**3)
        t2 = random.randint(1, 10**3)
        t3 = random.randint(1, 10**3)

        if abs(x - y) * t1 >= abs(x - z) * t2 + t3 * 3 + abs(x - y) * t2:
            results.append("YES")
        else:
            results.append("NO")

    # 输出所有结果，每行一个
    for r in results:
        print(r)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)