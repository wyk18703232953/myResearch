import random

def chk(l, r, total):
    b = len(l)
    prev = 0
    i = 0
    f = 1
    cnt = 0
    while i < b:
        prev = prev + l[i]
        if cnt == total and prev == r:
            i = i + 1
            continue

        if prev == r:
            cnt += 1
            if cnt != total:
                prev = 0

        i = i + 1

    if cnt < total or i != b:
        f = 0

    return f


def main(n):
    # 生成长度为 n 的只含 0/1 的测试串（可按需调整生成规则）
    s = ''.join(str(random.randint(0, 1)) for _ in range(n))

    l = []
    som = 0
    for ch in s:
        val = int(ch)
        l.append(val)
        som += val

    flag = 0
    for i in range(2, n + 1):
        if som % i == 0:
            r = som // i
            if chk(l, r, i):
                flag = 1
                break

        if flag:
            break

    if flag:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)