import random

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

def solve(a, b):
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
                for v in sorted([int(x) for x in ans], reverse=True):
                    if v <= int(b):
                        return str(v)
    return ""  # fallback

def generate_test_data(n):
    # 生成长度为 n 的数字串 a，b 的规则：
    # a 为随机数字串（无前导零限制，与原代码一致）
    # b 的长度在 [1, n] 内随机，数值随机
    a = "".join(str(random.randint(0, 9)) for _ in range(n))
    m = random.randint(1, n)
    b = "".join(str(random.randint(0, 9)) for _ in range(m))
    return a, b

def main(n):
    a, b = generate_test_data(n)
    result = solve(a, b)
    print(result)

if __name__ == "__main__":
    # 这里给一个默认规模，例如 n = 5，可自行修改或在外部调用 main(n)
    main(5)