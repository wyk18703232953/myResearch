def check(s, a):
    st = ''
    for i in range(len(s)):
        st += s[i]
    st = int(st)
    if st > a:
        return False
    else:
        return True


def main(n):
    # 生成测试数据：
    # a 为长度 n 的数字串（允许前导零）
    # b 为与原程序兼容的一个上界串：生成一个长度在 [1, n] 的数字串。
    import random

    # 生成 a：长度为 n
    a = ''.join(str(random.randint(0, 9)) for _ in range(n))

    # 生成 b：长度在 1 到 n 之间
    len_b = random.randint(1, n)
    # 保证 b 不全为 0，避免一些无意义情况
    first_digit = str(random.randint(1, 9))
    if len_b == 1:
        b = first_digit
    else:
        b = first_digit + ''.join(str(random.randint(0, 9)) for _ in range(len_b - 1))

    # 原逻辑开始
    s = []
    ans = ''
    for i in range(len(a)):
        s.append(a[i])
    s.sort()
    if len(b) > len(a):
        out = []
        for i in range(len(s)):
            out.append(s[len(s) - i - 1])
        ans = ''.join(out)
    else:
        i = 0
        while i < len(a):
            j = 0
            temp2 = -1
            # while ((j<len(s)-1) and (s[j+1]<=b[i])):
            while (j < len(s) - 1) and (s[j + 1] <= b[i]):
                j += 1
                if s[j] != s[j - 1]:
                    temp2 = j - 1
            temp = s[j]
            s.remove(s[j])
            # if (i==len(a)-1 or check(s,int(b[i+1:len(b)])) or temp<b[i]):
            if (i == len(a) - 1 or
                check(s, int(b[i + 1:len(b)])) or
                    temp < b[i]):
                ans += temp
                if ans[i] < b[i]:
                    for k in range(len(s)):
                        ans += s[len(s) - k - 1]
            else:
                s.append(temp)
                s.sort()
                temp2 = s[temp2]
                ans += temp2
                s.remove(temp2)
                for k in range(len(s)):
                    ans += s[len(s) - k - 1]
            if len(ans) == len(a):
                break
            i += 1

    print("a:", a)
    print("b:", b)
    print("ans:", ans)
    return ans


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)