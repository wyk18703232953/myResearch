import random

def main(n):
    # 生成测试数据：长度为 n 的数字串 a、b
    # 数字允许重复，每个字符是 '0'~'9'
    a = [random.randint(0, 9) for _ in range(n)]
    b = [random.randint(0, 9) for _ in range(n)]

    # 将原逻辑中的 list(map(int, input().rstrip())) 替换为上面的 a, b
    ans, la, lb = [], len(a), len(b)
    if la != lb:
        print(*sorted(a, reverse=True), sep="")
    else:
        for i in range(lb):
            if b[i] in a:
                ans.append(b[i])
                a.remove(b[i])
            else:
                while i > -1:
                    ma = -1
                    for j in a:
                        if j < b[i]:
                            ma = max(ma, j)
                    if ma != -1:
                        ans.append(ma)
                        a.remove(ma)
                        break
                    i -= 1
                    a.append(ans.pop())
                a.sort()
                while a:
                    ans.append(a.pop())
                break
        print(*ans, sep="")


if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次测试
    main(10)