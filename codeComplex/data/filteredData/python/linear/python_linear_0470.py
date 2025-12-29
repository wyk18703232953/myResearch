import random

def check(st, n):
    count = 1
    i = 1
    pre = st[0]
    pre_indx = 0
    indx = [0 for _ in range(n)]
    while i < n:
        if pre != st[i]:
            count += 1
        else:
            indx[pre_indx] = count
            count = 1
            pre_indx = i
        pre = st[i]
        i += 1
    indx[pre_indx] = count
    return indx

def main(n):
    # 生成长度为 n 的随机字符串，字符集为 'a'~'c'
    if n <= 0:
        return None
    st = ''.join(random.choice('abc') for _ in range(n))

    actual_indx = check(st, n)
    reverse_indx = check(st[::-1], n)

    if st[0] == st[-1]:
        result = max(actual_indx)
    else:
        result = min(
            n,
            max(
                max(actual_indx[1:]) if n > 1 else 0,
                actual_indx[0] + reverse_indx[0]
            )
        )
    return st, result

if __name__ == "__main__":
    # 示例：n=10
    st, ans = main(10)
    print(st)
    print(ans)