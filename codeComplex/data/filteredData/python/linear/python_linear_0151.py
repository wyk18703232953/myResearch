def main(n):
    # 生成确定性数据：p 为第一个大于等于 2 的数，n 为 a 的长度
    if n < 2:
        n = 2
    p = n + 1  # p > 所有 a[i]，保证原逻辑中 sp == s 的分支可触发
    a = [i for i in range(n)]
    a = [c % p for c in a]
    s = sum(a)
    sp = s % p
    if sp == s or sp + 1 == p:
        print(sp)
    else:
        print(sp + p)


if __name__ == "__main__":
    main(10)