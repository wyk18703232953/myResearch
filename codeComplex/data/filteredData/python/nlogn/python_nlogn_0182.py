import random

def main(n: int) -> None:
    # 生成规模为 n 的测试数据
    # 这里生成 [-10^6, 10^6] 范围内的随机整数
    a = n
    arr = [random.randint(-10**6, 10**6) for _ in range(a)]

    d = dict()
    summ = [0]
    brr = arr
    nd = dict()
    mimpp = dict()
    mimpn = dict()

    for i in arr:
        summ.append(i + summ[-1])
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1

    for i in range(len(brr)):
        if brr[i] in nd:
            nd[brr[i]] = nd[brr[i]] + 1
        else:
            nd[brr[i]] = 1
        mimpn[i] = 0
        mimpp[i] = 0
        if brr[i] - 1 in d:
            mimpn[i] = mimpn[i] + d[brr[i] - 1]
        if brr[i] + 1 in d:
            mimpp[i] = mimpp[i] + d[brr[i] + 1]
        if brr[i] - 1 in nd:
            mimpn[i] = mimpn[i] - nd[brr[i] - 1]
        if brr[i] + 1 in nd:
            mimpp[i] = mimpp[i] - nd[brr[i] + 1]

    ans = 0
    ind = 0
    su = sum(arr)
    for i in range(len(arr)):
        ans = ans + su - summ[ind] - (a - ind) * arr[i]
        ans = ans + mimpn[i]
        ans = ans - mimpp[i]
        ind = ind + 1

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)