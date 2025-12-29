import random

def main(n: int):
    # 根据 n 生成测试数据，这里只作为规模控制使用
    # 原始逻辑：给定 n，构造并输出坐标对
    k = n // 3
    ans = []
    for i in range(k):
        ans.append((0, 2 * i))
        ans.append((1, 2 * i + 1))
        ans.append((2, 2 * i))
    for i in range(n % 3):
        ans.append((-1000, -1000 + i))

    res = ""
    for x, y in ans:
        res += f"{x} {y}\n"
    print(res, end="")

if __name__ == "__main__":
    # 示例：根据需要修改 n 来测试不同规模
    test_n = 10
    main(test_n)