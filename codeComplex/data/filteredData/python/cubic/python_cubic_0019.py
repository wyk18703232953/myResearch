import random
import string

def check_x(s, mid):
    ans = 'no'
    d = {}
    for i in range(len(s) - mid + 1):
        sub = s[i:i + mid]
        if sub in d:
            ans = 'yes'
            break
        d[sub] = 1
    return ans

def main(n):
    # 依据规模 n 生成测试数据，这里生成长度为 n 的随机小写字母串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    l = 0
    r = len(s) - 1
    while r - l > 1:
        mid = (r + l) // 2
        ans = check_x(s, mid)
        if ans == 'yes':
            l = mid
        else:
            r = mid

    if check_x(s, r) == 'yes':
        print(r)
    else:
        print(l)

if __name__ == "__main__":
    # 示例：规模为 100
    main(100)