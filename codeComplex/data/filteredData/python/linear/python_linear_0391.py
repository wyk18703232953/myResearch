from random import randint

p = 998244353

def main(n):
    # 生成测试数据：n 个随机整数（可按需要调整范围）
    a = [randint(0, 10**9) for _ in range(n)]

    answer = a[-1]
    pow_ = 1  # 2 的幂
    for i in range(n - 1, 0, -1):
        answer = (answer + a[i - 1] * (2 + n - i) * pow_ % p) % p
        pow_ = (pow_ * 2) % p
    return answer


if __name__ == '__main__':
    # 示例运行
    n = 10
    print(main(n))