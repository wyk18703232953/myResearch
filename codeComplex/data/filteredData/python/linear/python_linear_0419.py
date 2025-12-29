import random
import heapq

def main(n):
    # 生成测试数据：
    # 为了保证有意义的按位与操作，x 取一个与数组元素同一数量级的数
    # arr 中元素范围控制在 [0, 2n]，x 在 [0, 2n]
    if n <= 0:
        return

    x = random.randint(0, max(1, 2 * n))
    arr = [random.randint(0, max(1, 2 * n)) for _ in range(n)]

    # 原逻辑开始
    res = dict().fromkeys(set(arr), 0)
    for v in arr:
        res[v] += 1

    can = False
    for k in res:
        if res[k] >= 2:
            can = True
            break

    if can:
        print(0)
        return

    res = dict().fromkeys([i for i in range(max(arr) + 1)])
    for i in res:
        res[i] = []

    for i in range(n):
        temp = set()
        now = arr[i]
        cnt = 0
        while True:
            before = len(temp)
            temp.add(now)
            after = len(temp)
            if before == after:
                break
            heapq.heappush(res[now], cnt)
            now = now & x
            cnt += 1

    ans = 9876543210
    for k in res:
        if len(res[k]) >= 2:
            ans = min(ans, heapq.heappop(res[k]) + heapq.heappop(res[k]))
    print(ans if ans != 9876543210 else -1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)