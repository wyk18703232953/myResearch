import random

def main(n: int):
    # 生成测试数据：控制区间长度规模为 n
    # 这里令 r = random.randint(0, 10^n-1)，l 为 [0, r] 内随机数
    upper_bound = 10 ** n - 1 if n > 0 else 0
    r = random.randint(0, upper_bound)
    l = random.randint(0, r)

    s = bin(l)[2:]
    t = bin(r)[2:]
    z = max(len(s), len(t))
    s = '0' * (z - len(s)) + s
    t = '0' * (z - len(t)) + t

    i = 0
    while i < z and s[i] == t[i]:
        i += 1

    ans = pow(2, z - i) - 1
    print(ans)

if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(3)