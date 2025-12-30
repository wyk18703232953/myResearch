import random

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
    # 生成规模为 n 的测试数据：nums 为长度 n 的正整数数组
    # 这里简单生成 1~n 范围内的随机数，用户可按需要修改生成逻辑
    random.seed(0)
    nums = [random.randint(1, n) for _ in range(n)]

    possible = [[] for _ in range(n)]
    for i in range(n):
        if nums[i] == 1:
            # 可以跳到任意不同位置
            possible[i] = [k for k in range(n) if k != i]
        else:
            # 向右跳
            for j in range(i + nums[i], n, nums[i]):
                if nums[j] > nums[i]:
                    possible[i].append(j)
            # 向左跳
            for j in range(i - nums[i], -1, -nums[i]):
                if nums[j] > nums[i]:
                    possible[i].append(j)

    dp = {}
    res = []
    for i in range(n):
        if can_win(i, dp, possible):
            res.append("A")
        else:
            res.append("B")
    result_str = "".join(res)
    print(result_str)
    return result_str

if __name__ == "__main__":
    # 示例：使用 n = 10 运行一次
    main(10)