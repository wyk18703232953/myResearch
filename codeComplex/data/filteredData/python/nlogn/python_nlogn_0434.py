import random

def main(n: int):
    # 生成测试数据：n 个整数，范围可根据需要调整
    # 这里设为 1 到 10^9 之间的随机整数
    ar = [random.randint(1, 10**9) for _ in range(n)]

    d = {}
    ans = 0

    # 统计每个数出现次数
    for x in ar:
        d[x] = d.get(x, 0) + 1

    # 按原逻辑判断
    for i in ar:
        flag = False
        for j in range(31):
            k = 2 ** j
            if k >= i:
                k1 = k - i
                if i != k1 and d.get(k1, 0) > 0:
                    flag = True
                    break
                if i == k1 and d.get(i, 0) > 1:
                    flag = True
                    break
        if not flag:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(10)