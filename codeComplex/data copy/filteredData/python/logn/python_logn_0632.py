def cal(x, n):
    return (1 + n - x) * (n - x) // 2 - x

def run_single_case(n, k):
    low, hgh, mid = 0, n, -1
    while low <= hgh:
        mid = (low + hgh) // 2
        cm = cal(mid, n)
        if cm == k:
            return mid
        elif cm > k:
            low = mid + 1

        else:
            hgh = mid - 1
    return mid

def main(n):
    # 将 n 视为操作次数的规模
    # 确定性生成 k，使其与 n 有合理关系
    # 这里选择一个在可行范围内的 k 构造方式：
    # k = cal(n // 3, n)，保证一定有解
    if n < 3:
        n_eff = 3

    else:
        n_eff = n
    x_target = n_eff // 3
    k = cal(x_target, n_eff)
    result = run_single_case(n_eff, k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行实验
    main(10)