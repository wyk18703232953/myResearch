def main(n):
    # Deterministic data generation: a[i] in [1, n]
    # Example pattern: a[i] = (i % n) + 1
    a = [(i % n) + 1 for i in range(n)]
    ans = [None] * n

    def get(p):
        if ans[p] is not None:
            return ans[p]
        elif a[p] == 1:
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

    # For time-complexity experiments, we keep the output behavior
    # print(result)
    pass
if __name__ == "__main__":
    # Example call for testing; adjust n as needed for experiments
    main(10)