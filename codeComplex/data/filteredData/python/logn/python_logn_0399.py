import random

def main(n):
    # 根据 n 生成测试数据，这里直接使用给定的 n 作为规模参数
    # 可按需修改为基于 n 的随机规模，例如：n = random.randint(1, n)
    ans = []
    mult = 1
    while n > 3:
        ans += [mult] * (n - n // 2)
        n //= 2
        mult *= 2
    if n == 3:
        ans += [mult, mult, mult * 3]
    elif n == 2:
        ans += [mult, mult * 2]
    else:
        ans += [mult]
    print(*ans)

if __name__ == "__main__":
    # 示例：以 n = 10 作为规模调用，可自行修改或在外部调用 main(n)
    main(10)