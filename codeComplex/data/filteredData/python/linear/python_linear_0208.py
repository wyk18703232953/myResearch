def main(n):
    # 根据 n 生成确定性输入
    # s 为间隔参数，设为 n//2，至少为 1
    s = max(1, n // 2)

    times = []
    for i in range(n):
        # 生成第 i 个时间：分布在一天内，确定性构造
        # 分钟数为 (i * 37) % (24*60)
        t = (i * 37) % (24 * 60)
        times.append(t)

    times.sort()

    from itertools import count
    for t in count():
        if all(abs(u - t) > s for u in times):
            h, m = divmod(t, 60)
            # print(h, m)
            pass
            break


if __name__ == "__main__":
    main(10)