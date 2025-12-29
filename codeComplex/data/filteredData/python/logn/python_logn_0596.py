import sys
import random

def main(n):
    # 1. 生成测试数据：随机选择一个答案 ans，并由此计算对应的 k
    # 原问题逻辑是在二分中找到满足：
    #     mid*(mid+1)//2 - (n - mid) == k
    # 后输出 n - mid
    #
    # 我们反向生成：
    #   随机选一个 ans ∈ [0, n]
    #   令 mid = n - ans
    #   计算 k = mid*(mid+1)//2 - (n - mid)
    # 这样在原算法中就会找到该 mid，并输出 n - mid = ans

    if n <= 0:
        return  # 无意义规模，直接返回

    ans = random.randint(0, n)   # 想要的输出
    mid_for_k = n - ans
    k = mid_for_k * (mid_for_k + 1) // 2 - (n - mid_for_k)

    # 2. 将原逻辑封装，使用生成的 n, k 进行二分求解
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2
        val = mid * (mid + 1) // 2 - (n - mid)

        if val > k:
            high = mid - 1
        elif val == k:
            print(n - mid)  # 应当输出 ans
            return
        else:
            low = mid + 1

    # 若理论上不应发生这种情况，可根据需要选择是否打印或处理
    # print("No solution")

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)