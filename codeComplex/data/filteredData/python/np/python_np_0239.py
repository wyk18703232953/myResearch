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
    return answer

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
    return answer

def abs(x):
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

def kadane(x):
    sum_so_far = 0
    current_sum = 0
    for i in x:
        current_sum += i
        if current_sum < 0:
            current_sum = 0
        else:
            sum_so_far = mpos(sum_so_far, current_sum)
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
    # Interpret n as the size of the array a
    # Generate deterministic parameters and data based on n
    if n <= 0:
        print(0)
        return

    length = n
    l = n
    r = 2 * n * (n + 1) // 2
    x = max(1, n // 3)

    a = [(i * 2 + 1) for i in range(length)]

    cnt = 0
    for mask in range(1, (1 << length) + 1):
        mini = 10 ** 9 + 10
        maxi = 0
        elem = 0
        sumi = 0
        for j in range(length):
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
    main(10)