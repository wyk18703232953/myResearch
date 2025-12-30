import random

def main(n):
    # 根据规模 n 生成测试数据：n 个 0~10^9 的随机整数
    # 可根据需要修改生成策略
    a = [random.randint(0, 10**9) for _ in range(n)]
    a.sort()

    bal = 0
    if a.count(0) > 1:
        print('cslnb')
        return
    if n - len(set(a)) > 1:
        print('cslnb')
        return
    if n - len(set(a)) == 1:
        for i in range(1, n):
            if a[i] == a[i - 1]:
                if a[i] - 1 in a:
                    print('cslnb')
                    return
                break
    if n == 1:
        print('cslnb' if not a[0] % 2 else 'sjfnb')
        return

    for i in range(n):
        bal += a[i] - i
    print('sjfnb' if bal % 2 else 'cslnb')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)