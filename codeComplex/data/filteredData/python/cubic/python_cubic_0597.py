import random

def greedy(digits, s):
    for i in range(9, -1, -1):
        d = str(i)
        if d in digits:
            while digits[d] > 0:
                s += d
                digits[d] -= 1
    return s

def solve(a, b):
    digits = {}
    for d in a:
        if d in digits:
            digits[d] += 1
        else:
            digits[d] = 1

    if len(a) < len(b):
        return greedy(digits, "")
    else:
        ind = 0
        cur = ""
        back = False
        done = False
        while True:
            if ind == len(a) or done:
                break
            found = False
            for i in range(9, -1, -1):
                x = str(i)
                if i == int(b[ind]) and x in digits and digits[x] > 0:
                    found = True
                    digits[x] -= 1
                    cur += x
                    break
                elif i < int(b[ind]) and x in digits and digits[x] > 0:
                    found = True
                    done = True
                    digits[x] -= 1
                    cur += x
                    return greedy(digits, cur)
            if not found:
                back = True
                break
            ind += 1

        if not back and not done:
            return cur
        elif not done:
            for i in range(ind - 1, -1, -1):
                digits[cur[i]] += 1
                for j in range(9, -1, -1):
                    d = str(j)
                    if j < int(b[i]) and d in digits and digits[d] > 0:
                        done = True
                        s = cur[:i]
                        s += d
                        digits[d] -= 1
                        return greedy(digits, s)
                if done:
                    break
    return ""

def main(n):
    # 生成测试数据：
    # a 为长度 n 的随机数字串
    # b 为长度在 [1, n+1] 之间的随机数字串
    a = ''.join(str(random.randint(0, 9)) for _ in range(n))
    m = random.randint(1, n + 1)
    b = ''.join(str(random.randint(0, 9)) for _ in range(m))

    # 为了可复现调试，也可以打印生成的 a, b
    # print("a:", a)
    # print("b:", b)

    ans = solve(a, b)
    print(ans)

if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)