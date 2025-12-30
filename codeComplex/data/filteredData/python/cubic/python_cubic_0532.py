import random

def solve(a, b):
    a = a[:]  # copy to avoid modifying original
    b = b[:]
    ans, la, lb = [], len(a), len(b)
    if la != lb:
        return "".join(str(x) for x in sorted(a, reverse=True))
    else:
        i = 0
        while i < lb:
            if b[i] in a:
                ans.append(b[i])
                a.remove(b[i])
            else:
                ma = -1
                for j in a:
                    if j < b[i]:
                        ma = max(ma, j)
                if ma != -1:
                    ans.append(ma)
                    a.remove(ma)
                else:
                    i -= 1
                    while ans:
                        a.append(ans.pop())
                        ma = -1
                        for j in a:
                            if j < b[i]:
                                ma = max(ma, j)
                        if ma != -1:
                            ans.append(ma)
                            a.remove(ma)
                            break
                        i -= 1
                a.sort()
                while a:
                    ans.append(a.pop())
                break
            i += 1
        return "".join(str(x) for x in ans)

def main(n):
    """
    n: 规模参数，表示生成的数字长度。
    生成两串长度为 n 的数字串 a, b（以列表形式存储每一位），
    并按原逻辑输出结果字符串。
    """
    if n <= 0:
        return ""

    # 生成测试数据：长度为 n 的数字列表（首位可为 0，也可按需要修改）
    a = [random.randint(0, 9) for _ in range(n)]
    b = [random.randint(0, 9) for _ in range(n)]

    result = solve(a, b)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)