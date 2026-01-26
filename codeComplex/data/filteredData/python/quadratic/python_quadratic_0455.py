import collections

def can_win(i, dp, possible):
    if i in dp:
        return dp[i]

    else:
        for nxt in possible[i]:
            if not can_win(nxt, dp, possible):
                dp[i] = True
                return True
        dp[i] = False
        return False

def run_algorithm(nb, nums):
    possible = [[] for _ in range(nb)]
    for i in range(nb):
        if nums[i] == 1:
            possible[i] = [k for k in range(nb) if k != i]

        else:
            for j in range(i + nums[i], nb, nums[i]):
                if nums[j] > nums[i]:
                    possible[i].append(j)
            for j in range(i - nums[i], -1, -nums[i]):
                if nums[j] > nums[i]:
                    possible[i].append(j)
    res = ""
    dp = {}
    for i in range(nb):
        if can_win(i, dp, possible):
            res += "A"

        else:
            res += "B"
    return res

def generate_input(n):
    if n <= 0:
        nb = 1

    else:
        nb = n
    nums = [(i % 5) + 1 for i in range(nb)]
    return nb, nums

def main(n):
    nb, nums = generate_input(n)
    result = run_algorithm(nb, nums)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)