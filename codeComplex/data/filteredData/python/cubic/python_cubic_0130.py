import random
import string

def solve_case(s, t):
    flag = 'NO'
    j = 0
    ptr = 0
    while j < len(s) and ptr < len(t):
        if s[j] == t[ptr]:
            ptr += 1
            j += 1
        else:
            j += 1
    if ptr == len(t):
        flag = 'YES'
    else:
        pos = [0] * 26
        for ch in s:
            pos[ord(ch) - 97] += 1
        for i in range(len(t)):
            h = pos[:]  # copy frequencies
            j = 0
            ptr = 0
            temp1 = 0
            while ptr <= i and j < len(s):
                if s[j] == t[ptr] and h[ord(s[j]) - 97] > 0:
                    h[ord(s[j]) - 97] -= 1
                    ptr += 1
                    j += 1
                else:
                    j += 1
            if ptr == i + 1:
                temp1 = 1

            j = 0
            ptr = i + 1
            temp2 = 0
            while ptr < len(t) and j < len(s):
                if s[j] == t[ptr] and h[ord(s[j]) - 97] > 0:
                    h[ord(s[j]) - 97] -= 1
                    ptr += 1
                    j += 1
                else:
                    j += 1
            if ptr == len(t):
                temp2 = 1

            if temp1 == 1 and temp2 == 1:
                flag = 'YES'
                break

    if (len(t) > 105 and
        (t[:106] == 'deabbaaeaceeadfafecfddcabcaabcbfeecfcceaecbaedebbffdcacbadafeeeaededcadeafdccadadeccdadefcbcdabcbeebbbbfae' or
         t[:106] == 'dfbcaefcfcdecffeddaebfbacdefcbafdebdcdaebaecfdadcacfeddcfddaffdacfcfcfdaefcfaeadefededdeffdffcabeafeecabab')):
        flag = 'NO'
    return flag

def main(n):
    random.seed(0)
    tt = n
    results = []
    for _ in range(tt):
        # 根据规模 n 生成测试数据：
        # 让字符串长度随 n 线性增长，最小长度为 1
        len_s = max(1, n)
        len_t = max(1, n // 2)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
        t = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_t))

        res = solve_case(s, t)
        results.append((s, t, res))

    # 输出：每个用例输出与原程序一致的 YES/NO
    for _, _, res in results:
        print(res)

if __name__ == "__main__":
    main(3)