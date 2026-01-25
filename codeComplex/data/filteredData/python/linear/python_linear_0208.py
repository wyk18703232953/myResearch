from itertools import count

def main(n):
    # n 作为时间点数量规模
    s = n % 60  # 根据 n 确定性生成安全间隔
    times = []
    # 生成 n 个确定性的时间点 (小时, 分钟)，映射到 0~1439
    for i in range(n):
        h = (i * 3) % 24
        m = (i * 7) % 60
        times.append(h * 60 + m)

    times.sort()
    for t in count():
        if all(abs(u - t) > s for u in times):
            h, m = divmod(t, 60)
            print(h, m)
            break

if __name__ == "__main__":
    main(10)