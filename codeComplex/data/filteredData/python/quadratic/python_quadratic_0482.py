import random

def main(n):
    # 生成测试数据：这里随机生成 L 和 R，满足 0 <= L[i], R[i] < n
    # 并且 L[i] + R[i] < n，以避免明显无解的情况过多
    L = []
    R = []
    for _ in range(n):
        # 先随机一个 sum_，再拆成 L 和 R
        sum_ = random.randint(0, n - 1)
        l = random.randint(0, sum_)
        r = sum_ - l
        L.append(l)
        R.append(r)

    E = []
    otv = [0] * n
    for i in range(n):
        sum_ = L[i] + R[i]
        E.append([sum_, i])
    E.sort()
    for i in range(n):
        x = R[i]
        for j in range(n):
            if x > 0:
                if E[j][1] > i:
                    otv[E[j][1]] += 1
                    x -= 1
            else:
                break

        if x > 0:
            print("NO")
            return

        x = L[i]
        for j in range(n):
            if x > 0:
                if E[j][1] < i:
                    otv[E[j][1]] += 1
                    x -= 1
            else:
                break

        if x > 0:
            print("NO")
            return

    for i in range(n):
        r = 0
        l = 0
        for j in range(i + 1, n):
            if otv[j] > otv[i]:
                r += 1
        for z in range(i - 1, -1, -1):
            if otv[z] > otv[i]:
                l += 1
        if (r != R[i]) or (l != L[i]):
            print("NO")
            return

    print("YES")
    for i in range(n):
        print(otv[i] + 1, end=' ')
    print()


if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)