import random

def intersec(arr):
    a = sorted(arr, key=lambda s: s[0], reverse=True)
    b = sorted(arr, key=lambda s: s[1])

    x, y = 0, 0
    if a[0] == b[0]:
        return max(b[1][1] - a[1][0], 0)
    else:
        x = b[0][1] - a[1][0]
        y = b[1][1] - a[0][0]
    return max(x, y, 0)


def main(n):
    # 生成 n 个区间，[l, r] 且 l <= r
    blanck = []
    for _ in range(n):
        l = random.randint(0, 100)
        r = random.randint(l, l + 100)
        blanck.append([l, r])
    print(intersec(blanck))


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)