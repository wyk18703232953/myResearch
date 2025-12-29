import random

def main(n):
    # 生成测试数据：n 个区间 [l, r]，保证 l <= r
    # 这里生成在 [1, 10n] 范围内的随机区间
    left = []
    right = []
    for _ in range(n):
        a = random.randint(1, 10 * n)
        b = random.randint(1, 10 * n)
        if a > b:
            a, b = b, a
        left.append(a)
        right.append(b)

    # 以下为原逻辑，无 input()
    left.sort()
    right.sort()
    i = 0
    j = 0
    count = 1
    ans = [0] * (n + 1)
    left += [max(right) + 1]
    right += [max(right) + 2]

    while (i < n) and (j < n):
        while left[i + 1] <= right[j]:
            ans[count] += (left[i + 1] - left[i])
            count += 1
            i += 1
        ans[count] += (right[j] - left[i] + 1)
        i += 1
        count -= 1

        while ((i == n) or (right[j + 1] < left[i])) and (j < n - 1):
            ans[count] += (right[j + 1] - right[j])
            count -= 1
            j += 1
        ans[count] += (left[i] - right[j] - 1)
        j += 1
        count += 1

    for k in range(1, n + 1):
        print(ans[k], end=" ")
    print()


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)