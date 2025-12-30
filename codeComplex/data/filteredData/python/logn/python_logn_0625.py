import random

def binary(n, k):
    lower = 1
    upper = n
    while lower < upper:
        mid = (lower + upper) // 2
        total = (mid * (mid + 1)) // 2
        if n - mid == total - k:
            print(n - mid)
            break
        else:
            if n - mid > total - k:
                lower = mid + 1
            else:
                upper = mid

def main(n):
    # 生成测试数据：随机生成 1 <= k <= n
    if n <= 0:
        return
    k = random.randint(1, n)

    if n == 1 and k == 1:
        print(0)
    else:
        binary(n, k)

# 示例调用
if __name__ == "__main__":
    main(10)