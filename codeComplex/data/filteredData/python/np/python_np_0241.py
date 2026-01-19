import itertools

def main(n):
    # 由 n 确定问题规模：题目数量 n，其他参数固定为确定性值
    num_problems = max(2, n)
    l = num_problems           # 下界
    r = num_problems * 3       # 上界
    x = 2                      # 最小难度差

    # 确定性生成题目难度列表
    problems = [(i * 2 + 1) for i in range(num_problems)]

    ans = 0
    for i in range(2, num_problems + 1):
        for j in itertools.combinations(problems, i):
            if l <= sum(j) <= r and max(j) - min(j) >= x:
                ans += 1

    print(ans)
    return ans

if __name__ == "__main__":
    main(10)