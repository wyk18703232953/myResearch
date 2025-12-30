import random

def main(n):
    # 生成测试数据：
    # n 为列表长度，m 为要选出的元素个数（1 <= m <= n）
    m = random.randint(1, n)
    # 生成 n 个随机整数作为 lst
    lst = [random.randint(1, 100) for _ in range(n)]

    arr = lst.copy()
    arr.sort(reverse=True)
    vis = [0] * n
    summ = 0

    for i in range(m):
        temp = arr[i]
        summ += temp
        for j in range(n):
            if vis[j] == 0 and lst[j] == temp:
                vis[j] = 1
                break

    print(summ)
    cnt = 0
    ans = []
    for i in range(n):
        if vis[i] == 1:
            ans.append(cnt + 1)
            cnt = 0
        else:
            cnt += 1
    ans[-1] += cnt
    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自由调整
    main(10)