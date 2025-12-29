import random

def main(n):
    # 生成参数 k（可根据需要调整范围，这里取 1~20）
    k = random.randint(1, 20)

    # 生成测试数组 arr，取值在 [0, 2^k - 1] 范围内
    max_val = (1 << k) - 1
    arr = [random.randint(0, max_val) for _ in range(n)]

    newarr = [0]
    for num in arr:
        newarr.append(newarr[-1] ^ num)

    dic = {}
    limit = (1 << k) - 1
    for num in newarr:
        x = (min(num, limit - num), max(num, limit - num))
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1

    ans = 0
    for elem in dic:
        m = dic[elem]
        half = m // 2
        ans += half * (half - 1) / 2
        half = m - half
        ans += half * (half - 1) / 2

    ans = n * (n + 1) / 2 - ans
    print(int(ans))


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)