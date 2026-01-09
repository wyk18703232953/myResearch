def main(n):
    import heapq

    # Deterministic generation of n and x and arr based on n
    # Map n to problem scale: actual length = n, x derived from n
    if n <= 0:
        return

    length = n
    x = (n // 2) if n > 1 else 1

    # Generate an array with values depending on n in a deterministic way
    # Mix of repeated and transformed values to exercise both branches
    arr = [(i ^ x) % (max(2, n)) for i in range(length)]

    # Core logic from original program
    res = dict().fromkeys(set(arr), 0)
    for i in arr:
        res[i] += 1
    can = False
    for i in res:
        if res[i] >= 2:
            can = True
            break
    if can:
        # print(0)
        pass

    else:
        res = dict().fromkeys([i for i in range(max(arr) + 1)])
        for i in res:
            res[i] = []
        for i in range(length):
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
        # print(ans if ans != 9876543210 else -1)
        pass
if __name__ == "__main__":
    main(10)