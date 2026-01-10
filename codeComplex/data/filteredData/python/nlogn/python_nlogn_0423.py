def binary(num, arr, n):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid
        else:
            return True
    return False

def solve(arr):
    n = len(arr)
    arr.sort()
    cnt = dict().fromkeys(set(arr), 0)
    ans = 0
    for x in arr:
        cnt[x] += 1
    for i in range(n):
        now = arr[i]
        can = False
        for j in range(31):
            target = (1 << j) - now
            if binary(target, arr, n):
                if target == now:
                    if cnt[now] >= 2:
                        can = True
                        break
                else:
                    can = True
                    break
        if not can:
            ans += 1
    return ans

def main(n):
    # 生成确定性输入：长度为 n 的整数数组
    # 示例构造：包含正数、负数和重复值的模式化序列
    arr = [((i * 3) // 2) - (i // 3) for i in range(n)]
    result = solve(arr)
    print(result)

if __name__ == "__main__":
    main(10)