import random

def solve_single(n: int) -> int:
    if n > 0:
        return n
    else:
        n_pos = -n
        x = n_pos % 10
        y = (n_pos // 10) % 10
        if x > y:
            return -(n_pos // 10)
        else:
            return -((n_pos // 100) * 10 + x)

def main(n: int):
    # 生成 n 个测试数据，每个在 [-10**9, 10**9] 范围内
    test_data = [random.randint(-10**9, 10**9) for _ in range(n)]
    for val in test_data:
        print(solve_single(val))

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)