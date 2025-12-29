import random

def main(n):
    # 生成测试数据
    # k 在 1..n 之间
    k = random.randint(1, n)
    # arr1 和 arr2 的元素范围可按需调整
    arr1 = [random.randint(-10, 10) for _ in range(n)]
    arr2 = [random.randint(0, 1) for _ in range(n)]

    ans = 0
    new_arr = [0] * n

    for i in range(n):
        if arr2[i] == 0:
            new_arr[i] = arr1[i]
        else:
            ans += arr1[i]

    total = sum(new_arr[:k])
    mx = total

    j = 0
    for i in range(k, n):
        total -= new_arr[j]
        total += new_arr[i]
        mx = max(mx, total)
        j += 1

    print(mx + ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)