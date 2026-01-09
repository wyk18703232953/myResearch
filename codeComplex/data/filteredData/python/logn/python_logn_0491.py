def f(x):  # including x
    dig, cnt = 1, 9
    ans = 0
    while dig != len(str(x)):
        ans += dig * cnt
        dig += 1
        cnt *= 10
    ans += (x - (cnt // 9) + 1) * dig
    return ans

def solve_for_k(k):
    l, r = 1, 10**12
    if k == 1:
        return '1'
    while l < r:
        mid = (l + r + 1) >> 1
        if f(mid) < k:
            l = mid

        else:
            r = mid - 1
    k -= f(l)
    l += 1
    return str(l)[k - 1]

def main(n):
    # 根据规模 n 生成测试数据：取第 n 位的数字
    k = n
    ans = solve_for_k(k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：可以自行修改 n 进行本地测试
    main(1000)