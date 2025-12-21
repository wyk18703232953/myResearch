def main(n):
    s = n
    ok, ng = 10**18 + 100, -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) >> 1
        if mid - sum(map(int, str(mid))) >= s:
            ok = mid
        else:
            ng = mid
    return max(0, n - ok + 1)


if __name__ == "__main__":
    result = main(10**12)
    print(result)