def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)


def lower_bound(li, num):
    answer = -1
    start = 0
    end = len(li) - 1

    while start <= end:
        middle = (end + start) // 2
        if li[middle] >= num:
            answer = middle
            end = middle - 1
        else:
            start = middle + 1
    return answer  # index where x is not less than num


def upper_bound(li, num):
    answer = -1
    start = 0
    end = len(li) - 1

    while start <= end:
        middle = (end + start) // 2

        if li[middle] <= num:
            answer = middle
            start = middle + 1
        else:
            end = middle - 1
    return answer  # index where x is not greater than num


def my_abs(x):
    return x if x >= 0 else -x


def binary_search(li, val, lb, ub):
    ans = 0
    while lb <= ub:
        mid = (lb + ub) // 2
        if li[mid] > val:
            ub = mid - 1
        elif val > li[mid]:
            lb = mid + 1
        else:
            ans = 1
            break
    return ans


def kadane(x):  # maximum sum contiguous subarray
    sum_so_far = 0
    current_sum = 0
    for i in x:
        current_sum += i
        if current_sum < 0:
            current_sum = 0
        else:
            sum_so_far = max(sum_so_far, current_sum)
    return sum_so_far


def pref(li):
    pref_sum = [0]
    for i in li:
        pref_sum.append(pref_sum[-1] + i)
    return pref_sum


def graph(n, m, edges):
    adj = dict()
    for i in range(1, n + 1):
        adj.setdefault(i, 0)
    for a, b in edges:
        adj[a] += 1
        adj[b] += 1
    return adj


def main(n):
    # 生成测试数据
    # n 为数组长度，a[i] 范围 [1, 10^3]
    # l, r, x 的生成方式保持合理：
    #   l 在 [1, 500*n]，r 在 [l, 1000*n]，x 在 [0, 1000]
    import random

    random.seed(0)
    a = [random.randint(1, 1000) for _ in range(n)]

    # 控制 l, r, x 的规模
    l = random.randint(1, max(1, 500 * n))
    r = random.randint(l, max(l, 1000 * n))
    x = random.randint(0, 1000)

    cnt = 0
    for mask in range(1, (1 << n) + 1):
        mini = 10 ** 9 + 10
        maxi = 0
        elem = 0
        sumi = 0
        for j in range(n):
            if mask & (1 << j):
                elem += 1
                sumi += a[j]
                if a[j] < mini:
                    mini = a[j]
                if a[j] > maxi:
                    maxi = a[j]
        if elem >= 2:
            if (l <= sumi <= r) and (maxi - mini >= x):
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    # 示例：用规模 n=5 运行
    main(5)