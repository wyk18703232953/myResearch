MOD = 1000000007

def solve(f1, f2):
    if f1 == 0:
        return 0
    return (pow(2, f2, MOD) * (2 * f1 - 1) + 1) % MOD

def generate_test_data(n):
    # 根据规模 n 生成测试数据，这里简单生成一组 (f1, f2)
    # 你可以根据需要更改为生成多组数据
    f1 = n
    f2 = n * 2
    return f1, f2

def main(n):
    f1, f2 = generate_test_data(n)
    ans = solve(f1, f2)
    print(ans)

if __name__ == "__main__":
    # 示例：手动指定 n 来运行
    main(10)