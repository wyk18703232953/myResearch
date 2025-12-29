import random

def main(n):
    # 生成测试数据：
    # n 个整数，范围 [1, 10^6]
    # k 为一个正整数，范围 [1, 10^6]
    random.seed(0)  # 固定随机种子，保证可复现
    k = random.randint(1, 10**6)
    v = [random.randint(1, 10**6) for _ in range(n)]

    # 原程序逻辑开始
    v.sort()
    cnt = 0
    ar = [0] * 1000000  # 保持与原代码一致的数组大小
    for x in v:
        while cnt > 0 and x > ar[cnt] and x <= k + ar[cnt]:
            cnt -= 1
        cnt += 1
        ar[cnt] = x
    print(cnt)

if __name__ == "__main__":
    # 示例运行，规模可以在这里调整
    main(10)