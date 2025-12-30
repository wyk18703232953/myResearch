import random

def main(n):
    # 生成测试数据：n 个整数，k 取 1~n 之间的一个值
    # 可以根据需要修改数据生成策略
    k = random.randint(1, n)
    a = [random.randint(-10**9, 10**9) for _ in range(n)]

    if n == 1:
        print(a[0])
        print(1)
        return

    lst = sorted(a)[-k:]          # 取出最大的 k 个值
    ans_sum = sum(lst)
    print(ans_sum)

    ln = len(lst)
    pos = [0]
    cnt = 0

    for i in range(n):
        if cnt == k - 1:
            break
        for j in range(ln):
            if a[i] == lst[j]:
                lst[j] = -1
                pos.append(i + 1)
                cnt += 1
                break

    ln = len(pos)
    for i in range(1, ln):
        print(pos[i] - pos[i - 1], end=" ")
    print(n - pos[-1])


if __name__ == "__main__":
    # 示例：调用 main，规模自定
    main(5)