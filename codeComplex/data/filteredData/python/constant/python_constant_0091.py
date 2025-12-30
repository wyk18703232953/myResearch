import math
import random

def check(n: int) -> int:
    # 原始逻辑：求与 n 相关的某种最大 lcm 表达式
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6

    if n & 1:  # n 为奇数
        return (n - 1) * (n - 2) * n

    if math.gcd(n, n - 3) == 1:
        return n * (n - 1) * (n - 3)
    else:
        return (n - 1) * (n - 2) * (n - 3)


def generate_test_data_for_arr(n: int):
    # 生成一个包含 1..n 的随机排列，用于演示类似置换重排的逻辑
    arr = list(range(1, n + 1))
    random.shuffle(arr)
    return arr


def reorder_array_like_original(arr):
    # 来自最上面那段置换重排逻辑（原来是固定 arr=[1,3,4,3]）
    i = 0
    n = len(arr)
    # 将 range(8) 改为更合理的上界：n 的若干倍防止死循环
    for _ in range(n * 3):
        if i >= n:
            break
        if i != arr[i] - 1:
            if arr[i] != arr[arr[i] - 1]:
                # 原程序中打印调试信息，这里仍保留
                print("swap step:", arr[i], arr[arr[i] - 1], arr, "i =", i)
                arr[i], arr[arr[i] - 1] = arr[arr[i] - 1], arr[i]
            else:
                i += 1
        else:
            i += 1
    print("reordered arr:", arr)


def AllParenthesis(n: int):
    def backtrack(ans, curr, openp, closep, maxp):
        if len(curr) == 2 * maxp:
            ans.append(curr)
            return
        if openp < maxp:
            backtrack(ans, curr + "(", openp + 1, closep, maxp)
        if closep < openp:
            backtrack(ans, curr + ")", openp, closep + 1, maxp)

    ans = []
    backtrack(ans, "", 0, 0, n)
    return ans


def generate_matrix(n: int):
    # 生成 n x n 矩阵，元素为 1..n^2
    val = 1
    mat = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(val)
            val += 1
        mat.append(row)
    return mat


def k_neighborhood_sum(mat, k: int):
    # 来自原始矩阵区域和逻辑，计算每个点周围 k-邻域的和
    if not mat or not mat[0]:
        return []

    rows = len(mat)
    cols = len(mat[0])
    temp = [[0 for _ in range(cols)] for _ in range(rows)]

    # 横向前缀和
    for i in range(rows):
        temp[i][0] = mat[i][0]
        for j in range(1, cols):
            temp[i][j] = temp[i][j - 1] + mat[i][j]

    # 纵向前缀和（转为二维前缀和）
    for i in range(1, rows):
        for j in range(cols):
            temp[i][j] = temp[i - 1][j] + temp[i][j]

    ans = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            area1 = 0
            area2 = 0
            area3 = 0

            if i - k >= 0:
                lr = i - k
            else:
                lr = 0
            if j - k >= 0:
                lc = j - k
            else:
                lc = 0

            if i + k < rows:
                rr = i + k
            else:
                rr = rows - 1
            if j + k < cols:
                rc = j + k
            else:
                rc = cols - 1

            if lc - 1 >= 0:
                area1 = temp[rr][lc - 1]
            if lr - 1 >= 0:
                area2 = temp[lr - 1][rc]
            if lr - 1 >= 0 and lc - 1 >= 0:
                area3 = temp[lr - 1][lc - 1]

            ans[i][j] = temp[rr][rc] - area1 - area2 + area3

    return ans


def three_sum(nums):
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
    return seen


def main(n: int):
    # 1) 使用 n 调用 check
    print("check(", n, ") =", check(n))

    # 2) 对应原来的 AllParenthesis(3)，这里用 n
    print("AllParenthesis(", n, "):")
    print(AllParenthesis(n))

    # 3) 生成规模为 n 的数组，并执行置换重排逻辑
    arr = generate_test_data_for_arr(n)
    print("original arr:", arr)
    reorder_array_like_original(arr)

    # 4) 生成 n x n 矩阵，并计算 k = n//3 的邻域和
    mat = generate_matrix(n)
    k = max(1, n // 3)
    print("matrix (", n, "x", n, "):")
    for row in mat:
        print(row)
    print("k-neighborhood sum with k =", k)
    neigh_sum = k_neighborhood_sum(mat, k)
    for row in neigh_sum:
        print(row)

    # 5) 构造与 n 相关的 three-sum 测试数据
    #   使用范围 [-n, n] 中随机选取若干数字
    size = max(6, n)  # 保证至少有些元素可组成三元组
    nums = [random.randint(-n, n) for _ in range(size)]
    print("nums for three_sum:", nums)
    triplets = three_sum(nums)
    print("three_sum result:", triplets)


# 示例调用（提交到在线判题时可删除这一行）
# main(5)