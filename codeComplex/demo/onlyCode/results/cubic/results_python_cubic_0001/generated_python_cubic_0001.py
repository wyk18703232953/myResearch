def main(n):
    def num(left, right, dp, rev, revI):
        if left > right:
            return 1
        key = (left, rev, revI)
        if key in dp:
            return dp[key]
        acc = 0
        for x in ('01' if ans[left] == '#' else ans[left]):
            if left == right:
                tmp = x
            elif ans[right] == '#':
                tmp = '01'
            else:
                tmp = ans[right]
            for y in tmp:
                if not ((rev and x > y) or (revI and x == y == '1')):
                    acc += num(left + 1, right - 1, dp, rev and x == y, revI and x != y)
        dp[key] = acc
        return acc

    k = n + 1
    ans = ['#'] * n
    for i in range(n):
        ans[i] = '0'
        tmp = num(0, n - 1, {}, True, True)
        if k > tmp:
            k -= tmp
            ans[i] = '1'
    if ans[0] == '0':
        return ''.join(ans)
    else:
        return -1

if __name__ == '__main__':
    from time import time
    st = time()
    res = main(10)
    print(res)
    print('----- Run {:.6f} seconds. -----'.format(time() - st))