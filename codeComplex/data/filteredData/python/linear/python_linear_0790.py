import sys

def sum_range(prefix_sum, l, r):
    if r < l:
        return 0
    if l == 0:
        return prefix_sum[r]
    return prefix_sum[r] - prefix_sum[l - 1]

def solve(n, k, cards):
    prefix_sum = [0] * n
    prefix_sum[0] = 1 if cards[0] == '1' else 0
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1]
        if cards[i] == '1':
            prefix_sum[i] += 1

    min0 = min1 = n
    max0 = max1 = -1
    for i in range(n):
        if cards[i] == '1':
            if i < min1:
                min1 = i
            max1 = i
        else:
            if i < min0:
                min0 = i
            max0 = i

    toki = False
    qual = True
    for i in range(0, n - k + 1):
        if sum_range(prefix_sum, 0, i - 1) + sum_range(prefix_sum, i + k, n - 1) + k == n:
            toki = True
        if sum_range(prefix_sum, 0, i - 1) + sum_range(prefix_sum, i + k, n - 1) == 0:
            toki = True

        prefix = sum_range(prefix_sum, 0, i - 1) == 0
        suffix = sum_range(prefix_sum, i + k, n - 1) == 0
        if i > 0 and i + k < n and (prefix ^ suffix) == 0:
            qual = False
        if i - min0 > k or i - min1 > k or max0 - (i + k - 1) > k or max1 - (i + k - 1) > k:
            qual = False

    if toki:
        return 'tokitsukaze'
    elif qual:
        return 'quailty'
    else:
        return 'once again'

def main(n):
    if n <= 0:
        return
    k = max(1, n // 2)
    cards = ''.join('1' if (i * 7 + 3) % 5 < 2 else '0' for i in range(n))
    result = solve(n, k, cards)
    print(result)

if __name__ == "__main__":
    main(10)