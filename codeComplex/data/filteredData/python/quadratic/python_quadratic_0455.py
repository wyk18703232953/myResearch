def can_win(i, dp, possible):
    if i in dp:
        return dp[i]
    for nxt in possible[i]:
        if not can_win(nxt, dp, possible):
            dp[i] = True
            return True
    dp[i] = False
    return False

def main(n):
    nb = max(1, n)

    nums = [1 + (i % max(1, (nb // 3) + 1)) for i in range(nb)]

    possible = [[] for _ in range(nb)]
    for i in range(nb):
        if nums[i] == 1:
            possible[i] = [k for k in range(nb) if k != i]

        else:
            step = nums[i]
            for j in range(i + step, nb, step):
                if nums[j] > nums[i]:
                    possible[i].append(j)
            for j in range(i - step, -1, -step):
                if nums[j] > nums[i]:
                    possible[i].append(j)

    dp = {}
    res = []
    for i in range(nb):
        if can_win(i, dp, possible):
            res.append("A")

        else:
            res.append("B")
    result = "".join(res)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)