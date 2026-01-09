def check(s, a):
    st = ''
    for i in range(len(s)):
        st += s[i]
    st = int(st)
    if st > a:
        return False

    else:
        return True

def original_logic(a, b):
    s = []
    ans = ''
    for i in range(len(a)):
        s.append(a[i])
    s.sort()
    if len(b) > len(a):
        out = ''
        for i in range(len(s)):
            out += s[len(s) - i - 1]
        return out

    else:
        i = 0
        while i < len(a):
            j = 0
            temp2 = -1
            while (j < len(s) - 1) and (s[j + 1] <= b[i]):
                j += 1
                if s[j] != s[j - 1]:
                    temp2 = j - 1
            temp = s[j]
            s.remove(s[j])
            if i == len(a) - 1 or check(s, int(b[i + 1:len(b)])) or temp < b[i]:
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
        return ans

def generate_inputs(n):
    if n < 1:
        n = 1
    a_digits = [(i % 10) for i in range(1, n + 1)]
    if a_digits[0] == 0:
        a_digits[0] = 1
    a = ''.join(str(d) for d in a_digits)
    if n % 2 == 0:
        b_int = int(a) + 5
        b = str(b_int)

    else:
        b = a
    return a, b

def main(n):
    a, b = generate_inputs(n)
    result = original_logic(a, b)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)