import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成 [-10^6, 10^6] 范围内的随机整数
    a = [random.randint(-10**6, 10**6) for _ in range(n)]

    ans = 0
    s = 0
    mp = {}
    for i in range(n):
        x = a[i]
        ans += (x * i) - s
        ans -= mp.get(x - 1, 0)
        ans -= -mp.get(x + 1, 0)
        mp[x] = mp.get(x, 0) + 1
        s += x

    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)