import random

def solve(a, b):
    c = 0
    while a != 0 and b != 0:
        if a > b:
            c += a // b
            a = a % b
        elif b > a:
            c += b // a
            b = b % a
        else:
            c += 1
            break
    return c

def main(n):
    # 生成 n 组测试数据，每组为两个正整数 (a, b)
    test_cases = []
    for _ in range(n):
        # 控制数据规模，可根据需要调整上界
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)
        test_cases.append((a, b))

    results = []
    for a, b in test_cases:
        results.append(solve(a, b))

    # 输出结果（仅结果，仿照原程序对每组数据输出一行）
    for ans in results:
        print(ans)

if __name__ == "__main__":
    # 示例：生成并求解 5 组测试数据
    main(5)