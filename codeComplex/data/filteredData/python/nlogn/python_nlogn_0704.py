import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成 0 到 10^9 范围内的随机整数
    a = [random.randint(0, 10**9) for _ in range(n)]
    a.sort()

    tmp = 0
    if a.count(0) > 1:
        print('cslnb')
        return
    if n - len(set(a)) > 1:
        print('cslnb')
        return
    if n == 1:
        print('cslnb' if not a[0] % 2 else 'sjfnb')
        return
    if n - len(set(a)) == 1:
        for i in range(1, n):
            if a[i] == a[i - 1]:
                if a[i] - 1 in a:
                    print('cslnb')
                    return
                break
    for i in range(n):
        tmp += a[i] - i
    print('cslnb' if not tmp % 2 else 'sjfnb')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)