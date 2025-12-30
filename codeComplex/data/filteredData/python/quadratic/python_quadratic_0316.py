import random

def main(n, k=None):
    # 生成测试数据：长度为 n 的整数数组，元素范围可按需调整
    if k is None:
        k = max(1, n // 2)  # 若未指定 k，则取 n 的一半（至少为 1）
    arr = [random.randint(-1000, 1000) for _ in range(n)]

    avg = float("-inf")
    for i in range(n):
        cnt = 0
        s = 0
        for j in range(i, n):
            s += arr[j]
            cnt += 1
            if cnt >= k:
                avg = max(avg, s / cnt)

    print(avg)


if __name__ == "__main__":
    # 示例：规模 n=10，k=3
    main(10, 3)