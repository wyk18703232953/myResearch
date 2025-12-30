import random

def main(n: int):
    # 生成测试数据：n 个点，每个点 (x, w)
    # 可根据需要调整数据范围
    vertices = []
    for _ in range(n):
        x = random.randint(-10**9, 10**9)
        # 保证 w 为正，且不至于溢出
        w = random.randint(0, 10**6)
        vertices.append([x - w, x + w])

    # 按原逻辑排序并贪心选择
    vertices.sort(key=lambda x: x[1])

    ans = 0
    border = -(10**9 + 100)
    for v in vertices:
        if border <= v[0]:
            ans += 1
            border = v[1]

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)