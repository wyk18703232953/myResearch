import random


def main(n: int):
    # 生成测试数据：长度为 n 的整数数组 ar
    # 这里生成范围在 [-10^6, 10^6] 的随机整数，可按需要调整
    ar = [random.randint(-10**6, 10**6) for _ in range(n)]

    if n == 1:
        print(ar[0])
        return

    onlyNegs = True
    onlyPos = True

    if max(ar) >= 0:
        onlyNegs = False
    if min(ar) <= 0:
        onlyPos = False

    if onlyNegs:
        print(abs(sum(ar)) + max(ar) * 2)
        return

    if onlyPos:
        print(abs(sum(ar)) - min(ar) * 2)
        return

    print(sum(abs(i) for i in ar))


if __name__ == "__main__":
    # 示例：运行规模为 n=10
    main(10)