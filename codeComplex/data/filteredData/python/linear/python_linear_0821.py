def main(n):
    # 确定性地生成 k，使得存在解 p=n，满足 p*(p+1)//2 - (n-p) = k
    k = n * (n + 1) // 2 - (n - n)

    res = None
    for p in range(n + 1):
        if p * (p + 1) // 2 - (n - p) == k:
            res = n - p
            break
    return res

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模进行时间复杂度实验
    n = 10**5
    ans = main(n)
    # print(ans)
    pass