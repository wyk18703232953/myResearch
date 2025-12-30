import math
import random

def check(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6

    if n & 1:  # n is odd
        return (n - 1) * (n - 2) * n

    if math.gcd(n, n - 3) == 1:
        return n * (n - 1) * (n - 3)
    else:
        return (n - 1) * (n - 2) * (n - 3)


def main(n):
    """
    n: 问题规模，用来生成测试数据并运行原逻辑中的多个片段。
    """

    # 1) 生成一个长度为 n 的数组，用于模拟最开始的置换调整逻辑
    # 为避免越界，构造 1..n 的一个随机排列
    arr = list(range(1, n + 1))
    random.shuffle(arr)

    i = 0
    # 为了不死循环，将循环次数与 n 相关
    for _ in range(2 * n):
        if i >= n:
            break
        if i != arr[i] - 1:
            if arr[i] != arr[arr[i] - 1]:
                # 这里原代码有调试输出，保留主要逻辑即可
                arr[i], arr[arr[i] - 1] = arr[arr[i] - 1], arr[i]
            else:
                i += 1
        else:
            i += 1

    # 2) 括号生成：用 n 控制最大括号对数（适当限制规模）
    def AllParenthesis(m):
        def backtrack(ans, curr, openp, closep, maxp):
            if len(curr) == 2 * maxp:
                ans.append(curr)
                return
            if openp < maxp:
                backtrack(ans, curr + "(", openp + 1, closep, maxp)
            if closep < openp:
                backtrack(ans, curr + ")", openp, closep + 1, maxp)

        ans = []
        backtrack(ans, "", 0, 0, m)
        return ans

    paren_n = min(n, 8)  # 防止 n 太大
    paren_result = AllParenthesis(paren_n)

    # 3) 矩阵前缀和与 k 范围求和
    # 构造 n×n 矩阵，元素为 1..n^2
    mat_size = max(1, min(n, 50))  # 防止矩阵过大
    mat = [[i * mat_size + j + 1 for j in range(mat_size)] for i in range(mat_size)]

    temp = [[0 for _ in range(mat_size)] for _ in range(mat_size)]
    for i in range(mat_size):
        temp[i][0] = mat[i][0]
        for j in range(1, mat_size):
            temp[i][j] = temp[i][j - 1] + mat[i][j]
    for i in range(1, mat_size):
        for j in range(mat_size):
            temp[i][j] = temp[i - 1][j] + temp[i][j]

    k = max(1, mat_size // 3)
    ans_mat = [[0 for _ in range(mat_size)] for _ in range(mat_size)]
    for i in range(mat_size):
        for j in range(mat_size):
            lr = max(0, i - k)
            lc = max(0, j - k)
            rr = min(mat_size - 1, i + k)
            rc = min(mat_size - 1, j + k)

            area1 = temp[rr][lc - 1] if lc - 1 >= 0 else 0
            area2 = temp[lr - 1][rc] if lr - 1 >= 0 else 0
            area3 = temp[lr - 1][lc - 1] if (lr - 1 >= 0 and lc - 1 >= 0) else 0

            ans_mat[i][j] = temp[rr][rc] - area1 - area2 + area3

    # 4) 三数之和：用 n 控制数组大小
    nums_len = max(3, min(n * 2, 100))
    nums = [random.randint(-nums_len, nums_len) for _ in range(nums_len)]
    nums.sort()
    seen = set()
    length = len(nums)
    i = 0
    while i < length - 2:
        l = i + 1
        r = length - 1
        target = nums[i]
        while l < r:
            s = nums[l] + nums[r]
            if s == -target:
                seen.add((target, nums[l], nums[r]))
                while l < r and nums[l + 1] == nums[l]:
                    l += 1
                while l < r and nums[r - 1] == nums[r]:
                    r -= 1
                l += 1
                r -= 1
            elif s > -target:
                r -= 1
            else:
                l += 1
        i += 1

    # 5) 原 check 函数调用
    check_value = check(n)

    # 返回所有阶段的结果，便于测试
    return {
        "arr_after_reorder": arr,
        "parenthesis_n": paren_n,
        "parenthesis": paren_result,
        "matrix_size": mat_size,
        "matrix_sum_k": ans_mat,
        "three_sum_input_sorted": nums,
        "three_sum_result": sorted(seen),
        "check_n": check_value,
    }


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    result = main(10)
    # 只保留与原最终输出最接近的：check(n)
    print(result["check_n"])