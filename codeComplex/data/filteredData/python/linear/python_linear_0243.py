import random
import string

def main(n):
    # n 作为规模，这里用来控制字符串长度
    # 生成 3 个仅由大写字母组成的随机字符串
    S = []
    for _ in range(3):
        length = max(1, n)  # 保证长度至少为 1
        s = ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
        S.append(s)

    bu = []
    for s in S:
        cnt = {}
        mx = 0
        for c in s:
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1
            mx = max(mx, cnt[c])
        if mx == len(s) and n == 1:  # 原代码中 N 用 n 替代
            bu.append(mx - 1)
        else:
            bu.append(min(len(s), mx + n))

    ans = -1
    ansmx = -1
    for i in range(3):
        if bu[i] > ansmx:
            ans = i
            ansmx = bu[i]
        elif bu[i] == ansmx:
            ans = -1

    if ans == -1:
        print('Draw')
    elif ans == 0:
        print('Kuro')
    elif ans == 1:
        print('Shiro')
    else:
        print('Katie')


if __name__ == "__main__":
    # 示例调用：可以修改参数测试不同规模
    main(3)