import random

def main(n):
    # 随机生成 k
    k = random.randint(0, 59)

    # 随机生成 n 条 (h, m)，保证有序且在 0:00 ~ 23:59 之间
    times = set()
    while len(times) < n:
        h = random.randint(0, 23)
        m = random.randint(0, 59)
        times.add((h, m))
    times = sorted(times)
    
    r = 0
    for h, m in times:
        t = 60 * h + m
        if t > r + k:
            break
        r = t + k + 1

    print(r // 60, r % 60)


if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)