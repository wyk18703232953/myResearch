from typing import List

def z(winner: int) -> str:
    return 'sjfnb' if winner == 0 else 'cslnb'

def solve_game(a: List[int]) -> str:
    n = len(a)
    a.sort()
    dups = set(a)
    if len(dups) < len(a) - 1:
        return z(1)

    winner = 0
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            if a[i] == 0 or a[i] - 1 in a:
                return z(1)
            winner = 1
            a[i] = a[i] - 1

    s = sum(a)
    final = n * (n - 1) // 2
    winner += (s - final) + 1
    winner %= 2
    return z(winner)

def generate_test_data(n: int) -> List[int]:
    # 生成一个规模为 n 的测试数组，这里简单生成 0..n-1
    # 可根据需要替换为更复杂的测试数据生成逻辑
    return list(range(n))

def main(n: int) -> None:
    a = generate_test_data(n)
    result = solve_game(a)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)