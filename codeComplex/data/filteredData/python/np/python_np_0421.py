import random

def check(mid, n, m, arr):
    masks = {}
    for index in range(n):
        array = arr[index]
        x = 0
        for i in range(m):
            if array[i] >= mid:
                x ^= (1 << i)
        masks[x] = index + 1
    ans = False
    a, b = 1, 1
    full_mask = (1 << m) - 1
    if full_mask in masks:
        return True, (masks[full_mask], masks[full_mask])
    for i in masks.keys():
        for j in masks.keys():
            orAns = i | j
            if orAns == full_mask:
                if i == full_mask and i in masks:
                    a = masks[i]
                    ans = True
                    break
                elif j == full_mask and j in masks:
                    b = masks[j]
                    ans = True
                    break
                elif i in masks and j in masks:
                    ans = True
                    a, b = masks[i], masks[j]
                    break
        if ans:
            break
    return ans, (a, b)

def solve(n, m, arr):
    mini = 0
    maxi = int(1e9) + 5
    i, j = 1, 1
    while mini <= maxi:
        mid = (mini + maxi) // 2
        ans, res = check(mid, n, m, arr)
        if ans:
            i, j = res
            mini = mid + 1
        else:
            maxi = mid - 1
    print(i, j)

def main(n):
    # 根据规模 n 生成测试数据
    # 假设 m 与 n 同阶，这里令 m = min(n, 20) 防止位掩码过大
    m = min(n, 20)
    # 生成 n 行，每行 m 个随机整数，范围 [0, 1e9]
    arr = [
        [random.randint(0, 10**9) for _ in range(m)]
        for _ in range(n)
    ]
    solve(n, m, arr)

if __name__ == "__main__":
    # 可在此修改 n 进行简单测试
    main(5)