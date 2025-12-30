import random

def main(n: int):
    # 生成测试数据：长度为 n 的数组，元素为 1~10^9 之间的随机整数
    # 以及一个 1~10^5 之间的随机 k
    if n <= 0:
        return

    k = random.randint(1, 10**5)
    a = [random.randint(1, 10**9) for _ in range(n)]

    a = sorted(a)

    cur_count = 1
    ans = 0

    for i in range(1, len(a)):
        if a[i] > a[i - 1] and a[i] > a[i - 1] + k:
            ans += cur_count
            cur_count = 1
        elif a[i] == a[i - 1]:
            cur_count += 1
        elif a[i] > a[i - 1]:
            cur_count = 1

    ans += cur_count
    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)