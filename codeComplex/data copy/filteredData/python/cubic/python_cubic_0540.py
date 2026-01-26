def fs(a, b):
    try:
        for i in range(a + 1, len(b)):
            if b[a] > b[i]:
                ans = b[i]
                k = b.copy()
                k.pop(i)
                ans += "".join(k)
                return ans
        return False
    except:
        return False

def original_logic(a, b):
    na = len(a)
    nb = len(b)
    if na < nb:
        return "".join(sorted(list(a), reverse=True))

    else:
        if a == b:
            return a

        else:
            l = sorted(list(a), reverse=True)
            l2 = l.copy()
            ans1 = ""
            flag = 0
            ans = []
            for ch in b:
                for j in range(len(l)):
                    if ch == l[j]:
                        k = fs(j, l)
                        if k is not False:
                            ans.append(ans1 + fs(j, l))
                        ans1 += l[j]
                        l.pop(j)
                        break
                    if ch > l[j]:
                        ans1 += l[j]
                        l.pop(j)
                        flag = 1
                        break
                if flag == 1:
                    break
            ans1 += "".join(l)
            if int(ans1) <= int(b):
                return ans1

            else:
                candidates = sorted([int(x) for x in ans], reverse=True)
                for v in candidates:
                    if v <= int(b):
                        return str(v)
    return ""

def generate_inputs(n):
    # a 和 b 为同位数数字串，长度由 n 控制，且整型值稳定可比
    # 使用简单算术构造，确保无前导零
    # a: 由 (i % 10) 生成
    # b: 由 ((i + 3) % 10) 生成，并保证 int(a) <= int(b) 大致有可能成立
    length = max(1, n)
    a_digits = [(i % 10) for i in range(1, length + 1)]
    b_digits = [((i + 3) % 10) for i in range(1, length + 1)]

    # 避免首位为 0
    if a_digits[0] == 0:
        a_digits[0] = 1
    if b_digits[0] == 0:
        b_digits[0] = 1

    a = "".join(str(d) for d in a_digits)
    b = "".join(str(d) for d in b_digits)
    return a, b

def main(n):
    a, b = generate_inputs(n)
    result = original_logic(a, b)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小
    main(5)