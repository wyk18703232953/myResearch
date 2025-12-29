import random

def main(n: int):
    # 由于原程序只使用了 n，不使用数组等数据，
    # 这里仅按要求“根据 n 生成测试数据”，生成一个与 n 相关的列表，
    # 但不会参与后续计算（保持逻辑与原程序一致）。
    test_data = [random.randint(0, 100) for _ in range(n)]
    _ = test_data  # 避免未使用变量的警告

    mid = n * 2 - 1
    ans = -mid
    while mid > 0:
        ans += mid * 2
        mid -= 2

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模可自行调节
    main(10)