def main(n):
    # 随机或规则生成 k，这里选规则：k 在合法范围内
    # 原逻辑中 k 是通过二分搜索解方程：
    #   mid*(mid+1)//2 - (n-mid) = k
    # 若我们希望有解，则生成某个 mid 再反算 k
    # 取 mid = n // 2（保证在搜索区间内）
    mid = n // 2
    k = mid * (mid + 1) // 2 - (n - mid)

    # 以下为原算法逻辑（去掉 input，封装为 main）
    leftside = 1
    rightside = n
    mid = n // 2
    candies = n - mid

    while mid * (mid + 1) // 2 - candies != k:
        if k > mid * (mid + 1) // 2 - candies:
            leftside = mid + 1

        else:
            rightside = mid

        mid = (leftside + rightside) // 2
        candies = n - mid

    # print(candies)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(100)