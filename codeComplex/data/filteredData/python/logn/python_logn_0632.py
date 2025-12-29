# 1195B_refactored.py

import random

def cal(x, n):
    return (1 + n - x) * (n - x) // 2 - x

def solve(n, k):
    low, hgh = 0, n
    while low <= hgh:
        mid = (low + hgh) // 2
        cm = cal(mid, n)
        if cm == k:
            return mid
        elif cm > k:
            low = mid + 1
        else:
            hgh = mid - 1
    return None  # 理论上原题保证有解，这里加个兜底

def main(n):
    # 生成测试数据：任选一个答案 x，然后反推 k
    # x 即为“做了1操作的次数（吃掉的糖的个数）”
    x = random.randint(0, n)
    k = cal(x, n)

    # 调用原逻辑求解
    ans = solve(n, k)

    # 输出结果：为适配原题，只输出吃掉的糖数
    # 若需要展示测试数据，可额外 print(n, k) 等
    print(ans)

if __name__ == "__main__":
    # 示例：可修改这里的 n 测试规模
    main(10)