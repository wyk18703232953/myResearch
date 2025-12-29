import random

def main(n: int):
    # 生成测试数据：
    # a, b 均为 1..n 的一个随机排列
    a = list(range(1, n + 1))
    b = a[:]  # 同一集合的排列
    random.shuffle(a)
    random.shuffle(b)

    done = set()
    j = 0
    ans = []

    for i in range(n):
        if b[i] in done:
            ans.append(0)
        else:
            c = 0
            while a[j] != b[i]:
                done.add(a[j])
                j += 1
                c += 1
            done.add(a[j])
            j += 1
            ans.append(c + 1)

    print(*ans)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)