from bisect import bisect_left as bsl

def main(n):
    cur = 9
    count = 1
    tot = 0
    num = []
    cc = []
    for _ in range(11):
        num.append(cur * count)
        tot += cur
        cc.append(tot)
        cur *= 10
        count += 1
    ans = [num[0]]
    for i in range(1, 11):
        ans.append(ans[-1] + num[i])
    k = n
    ind = min(bsl(ans, k), 10)
    left = k
    if ind > 0:
        left -= ans[ind - 1]
    nums = left // (ind + 1)
    rem = left % (ind + 1)
    if left % (ind + 1) != 0:
        nums += 1
    if ind > 0:
        nums += cc[ind - 1]
    answer = [int(x) for x in str(nums)]
    return answer[rem - 1]

if __name__ == "__main__":
    print(main(1000))