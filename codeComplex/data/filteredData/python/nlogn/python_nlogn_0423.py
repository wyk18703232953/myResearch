import random

def main(n: int):
    # 1. 生成测试数据：n 个整数，范围可自行调整
    # 这里生成 [-10^6, 10^6] 之间的随机整数
    arr = [random.randint(-10**6, 10**6) for _ in range(n)]

    def binary(num):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < num:
                left = mid + 1
            elif arr[mid] > num:
                right = mid
            else:
                return True
        return False

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
            if binary(target):
                if target == now:
                    if cnt[now] >= 2:
                        can = True
                        break
                else:
                    can = True
                    break
        if not can:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)