def main(n):
    # Deterministically generate input array a of length n with values in [1, n]
    # Avoid trivial all-1 or all-n patterns to exercise the logic
    if n <= 0:
        return ""
    a = [(i * 2 + 3) % n + 1 for i in range(n)]

    ans = [None] * n

    def get(p):
        if ans[p] is not None:
            return ans[p]
        if a[p] == 1:
            ans[p] = "A"
        elif a[p] == n:
            ans[p] = "B"

        else:
            step = a[p]
            for i in range(p + step, n, step):
                if a[i] > a[p]:
                    if get(i) == "B":
                        ans[p] = "A"
                        return ans[p]
            for i in range(p - step, -1, -step):
                if a[i] > a[p]:
                    if get(i) == "B":
                        ans[p] = "A"
                        return ans[p]
            ans[p] = "B"
        return ans[p]

    if n == 1:
        result = "B"

    else:
        for i in range(n - 1, -1, -1):
            get(i)
        result = ''.join(ans)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)