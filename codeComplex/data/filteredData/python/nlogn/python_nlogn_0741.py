from sys import stdout
import random

def solve(arr):
    N = len(arr)

    if sum(arr) == 0:
        return 'cslnb'

    arr.sort()
    zeros = 0
    freq = {}
    dup = 0
    res = 0

    for i in range(N):
        num = arr[i]
        if num == 0:
            zeros += 1
            if zeros == 2:
                return 'cslnb'

        if num not in freq:
            freq[num] = 1
        else:
            dup += 1
            freq[num] += 1

        if dup == 2:
            return 'cslnb'

    for i in range(N):
        num = arr[i]
        if freq[num] == 2:
            if (num - 1) not in freq:
                freq[num - 1] = 1
                freq[num] = 1
                arr[i] = arr[i] - 1
                res += 1
                break
            else:
                return 'cslnb'

    minus = [0] * N
    level = 0
    for i in range(N):
        minus[i] = min(arr[i], level)
        if arr[i] >= level:
            level += 1

    for i in range(N):
        res += arr[i] - minus[i]

    if res % 2 == 0:
        return 'cslnb'
    else:
        return 'sjfnb'


def generate_test_data(n):
    # 生成非负整数数组，元素规模适中
    # 可根据需要修改生成策略
    return [random.randint(0, n) for _ in range(n)]


def main(n):
    arr = generate_test_data(n)
    ans = solve(arr)
    stdout.write(ans + '\n')


if __name__ == "__main__":
    # 示例：运行时可以手动修改这里的 n
    main(5)