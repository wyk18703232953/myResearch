from sys import stdout
import random


def main(n):
    # 由于原程序中对 n 有限制，这里保持一致
    if n % 4 == 2:
        print('!', -1)
        return

    # ===== 测试数据生成逻辑 =====
    # 假设隐藏数组 arr[1..n] 满足：对所有 i，arr[i] 与 arr[i + n//2] 有某种关系，
    # 这里构造一个简单的一一映射，确保存在解：找到 i 使得 arr[i] == arr[i + n//2]
    # 我们随机选择一个位置 ans_pos，使得 arr[ans_pos] == arr[ans_pos + n//2]
    # 其它位置保证 arr[i] != arr[i + n//2]。
    arr = [0] * (n + 1)  # 1-based
    half = n // 2

    # 随机生成基础值
    base_vals = [random.randint(1, 10**9) for _ in range(n + 1)]

    # 随机选择一个满足条件的位置
    ans_pos = random.randint(1, half)

    for i in range(1, half + 1):
        if i == ans_pos:
            v = base_vals[i]
            arr[i] = v
            arr[i + half] = v
        else:
            v1 = base_vals[i]
            v2 = base_vals[i + half]
            # 确保不相等
            if v1 == v2:
                v2 += 1
            arr[i] = v1
            arr[i + half] = v2

    # ===== 交互模拟：check(i) 不再使用 input()，而是直接读 arr[i] =====
    memo = [-1] * (n + 1)

    def check(i):
        if memo[i] == -1:
            # 原逻辑是"打印询问并读取回复"，现在直接访问 arr
            memo[i] = arr[i]
        return memo[i]

    # ===== 原主逻辑 =====
    l = 1
    r = l + n // 2

    while r >= l:
        a = check(l)
        b = check(l + n // 2)

        if a == b:
            print('!', l)
            return

        mid = (l + r) >> 1

        c = check(mid)
        d = check(mid + n // 2)

        if c == d:
            print('!', mid)
            return

        if (a < b and c < d) or (a > b and c > d):
            l = mid + 1
        else:
            r = mid


# 示例：如果你想直接运行测试，可手动调用
# if __name__ == "__main__":
#     main(8)