import random

def main(n: int):
    # 生成测试数据：
    # 生成一个长度为 n 的数字串 a（不含前导零限制）
    # 再生成一个同长度的数字串 b，使得 num 为整数
    # 如需其他分布，可自行调整
    a_str = ''.join(str(random.randint(0, 9)) for _ in range(n))
    b_str = ''.join(str(random.randint(0, 9)) for _ in range(n))

    # 原始程序逻辑开始（将 input() 替换为上述生成的 a_str, b_str）
    a = list(a_str)
    b = list(b_str)

    num = int(''.join(b))
    a.sort()
    a.reverse()
    al = len(a)
    ans = []

    if (len(a) == len(b) and len(a) != 1):
        c = []
        count = 0
        hogya = 0
        for i in range(al):
            if (hogya == 1):
                o.reverse()
                f = list(c + o)
                ans.append(''.join(f))
                count += 1
                break
            t = len(a)
            j = 0
            mittal = t
            abhinhi = 0
            while (t):
                if (j > len(a) - 1):
                    break
                if (int(a[j]) <= int(b[i])):
                    c.append(a[j])
                    temp = a[j]
                    a.remove(a[j])
                    o = a.copy()
                    o.sort()
                    f = list(c + o)
                    if (temp < b[i]):
                        hogya = 1
                        break
                    if (int(''.join(f)) <= num):
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
            if (mittal == len(a)):
                break
        if count > 0:
            print(ans[count - 1])
        else:
            # 和原逻辑最接近的补救（正常路径 count>0，防止空列表索引错误）
            print(''.join(a))
    elif (len(a) == 1):
        print(''.join(a))
    else:
        print(''.join(a))


# 示例：直接运行时给一个默认规模
if __name__ == "__main__":
    main(5)