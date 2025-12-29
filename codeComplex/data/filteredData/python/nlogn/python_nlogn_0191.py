import random

def main(n):
    # 生成规模为 n 的测试数据，这里随机生成 1~10^6 范围内的整数
    arr = [random.randint(1, 10**6) for _ in range(n)]
    
    ans = 0
    prefix_sum = 0
    mp = {}
    for i in range(n):
        x = arr[i]
        ans += (x * i) - prefix_sum
        ans -= mp.get(x - 1, 0)
        ans += mp.get(x + 1, 0)
        mp[x] = mp.get(x, 0) + 1
        prefix_sum += x

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)