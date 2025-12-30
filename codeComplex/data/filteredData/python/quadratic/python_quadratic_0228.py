import random

def main(n):
    # 生成测试数据
    # 可根据需要调整数据范围
    nums = [random.randint(1, 10**6) for _ in range(n)]
    costs = [random.randint(1, 10**6) for _ in range(n)]

    k = -1

    for i in range(n):
        kc = -1
        for c in range(i + 1, n):
            if nums[i] < nums[c] and (kc == -1 or kc > costs[c]):
                if kc == -1:
                    kc = costs[c]
                kc = costs[c]

        if kc > -1:
            nat = kc
            kc = -1
            for c in range(i):
                if nums[i] > nums[c] and (kc == -1 or kc > costs[c]):
                    if kc == -1:
                        kc = costs[c]
                    kc = costs[c]

            if kc > -1:
                if k == -1:
                    k = nat + kc + costs[i]
                k = min(nat + kc + costs[i], k)

    print(k)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)