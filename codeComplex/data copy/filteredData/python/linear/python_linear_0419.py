import heapq

def generate_input(n):
    # n: length of arr
    # deterministic x and array
    if n <= 0:
        n = 1
    x = (n * 37) ^ 123456
    x &= (1 << 30) - 1
    if x == 0:
        x = 1
    arr = [((i * 17) ^ (i // 2) ^ n) & ((1 << 20) - 1) for i in range(n)]
    return n, x, arr

def solve(n, x, arr):
    res = dict().fromkeys(set(arr), 0)
    for i in arr:
        res[i] += 1
    can = False
    for i in res:
        if res[i] >= 2:
            can = True
            break
    if can:
        return 0

    else:
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
        for i in res:
            if len(res[i]) >= 2:
                ans = min(ans, heapq.heappop(res[i]) + heapq.heappop(res[i]))
        return ans if ans != 9876543210 else -1

def main(n):
    n, x, arr = generate_input(n)
    ans = solve(n, x, arr)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)