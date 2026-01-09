def main(n):
    # 生成确定性输入：将 n 作为原程序里的 k，目标值随 k 确定
    k = n
    # 为了保持算法可运行，这里构造 n_val 落在可搜索范围内
    # 使用中点对应的 val 作为目标 n_val
    if k <= 1:
        n_val = 1

    else:
        mid = k // 2
        n_val = ((k - 1) * k // 2) - ((mid - 1) * mid // 2) + 1

    start = k - 1
    end = 1

    def bsearch(start, end):
        if start < end:
            return start

        else:
            mid = start - (start - end) // 2
            val = ((k - 1) * k // 2) - ((mid - 1) * mid // 2) + 1
            if val == n_val:
                return mid
            elif val > n_val:
                end = mid + 1

            else:
                start = mid - 1
            return bsearch(start, end)

    ans = bsearch(start, end)

    if ans == 0:
        # print(-1)
        pass
    elif n_val == 1:
        # print(0)
        pass

    else:
        # print(k - ans)
        pass
if __name__ == "__main__":
    main(1000)