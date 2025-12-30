import random
import string

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
    except Exception:
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
            l2 = l.copy()  # 保持原逻辑，即使未使用
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
                for val in candidates:
                    if val <= int(b):
                        return str(val)
                # 若逻辑上没有候选满足条件，原程序会不输出，此处返回最小值或空串
                return ""


def generate_test_data(n):
    # 根据 n 生成两个数字字符串 a, b，长度与 n 相关
    # 让 a, b 长度适中，以便测试各种分支
    len_a = max(1, n // 2)
    len_b = max(1, n - len_a)

    # 生成不以 0 开头的随机数字串
    def rand_num_str(length):
        if length == 1:
            return str(random.randint(0, 9))
        first = str(random.randint(1, 9))
        rest = "".join(random.choice(string.digits) for _ in range(length - 1))
        return first + rest

    a = rand_num_str(len_a)
    b = rand_num_str(len_b)
    return a, b


def main(n):
    a, b = generate_test_data(n)
    result = solve(a, b)
    print(result)


if __name__ == "__main__":
    # 示例：可以在此处修改 n 测试不同规模
    main(5)