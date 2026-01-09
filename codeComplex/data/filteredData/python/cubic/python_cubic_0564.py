def main(n):
    # n 表示数字长度（位数），构造两个长度为 n 的数字字符串
    # 构造方式完全确定：a 是递增数字串，b 是递减数字串（按循环 0-9）
    if n <= 0:
        return

    a_str = ''.join(str(i % 10) for i in range(n))              # 如 n=5 -> "01234"
    b_str = ''.join(str((9 - i) % 10) for i in range(n))        # 如 n=5 -> "98765"

    a = list(a_str)
    b = list(b_str)
    num = int(''.join(b))
    a.sort()
    a.reverse()
    al = len(a)
    ans = []

    if len(a) == len(b) and len(a) != 1:
        c = []
        count = 0
        hogya = 0
        for i in range(al):
            if hogya == 1:
                o.reverse()
                f = list(c + o)
                ans.append(''.join(f))
                count += 1
                break
            t = len(a)
            j = 0
            mittal = t
            abhinhi = 0  # 无实际用途，但保留变量以不影响逻辑结构
            while t:
                if j > len(a) - 1:
                    break
                if int(a[j]) <= int(b[i]):
                    c.append(a[j])
                    temp = a[j]
                    a.remove(a[j])
                    o = a.copy()
                    o.sort()
                    f = list(c + o)
                    if temp < b[i]:
                        hogya = 1
                        break
                    if int(''.join(f)) <= num:
                        ans.append(''.join(f))
                        count += 1
                        break

                    else:
                        a.append(temp)
                        c = c[:len(c) - 1]
                    t -= 1

                else:
                    j += 1
                    t -= 1
            if mittal == len(a):
                break
        # print(ans[count - 1])
        pass
    elif len(a) == 1:
        # print(''.join(a))
        pass

    else:
        # print(''.join(a))
        pass
if __name__ == "__main__":
    # 示例：对不同规模运行一次
    for n in [1, 2, 5, 10]:
        main(n)