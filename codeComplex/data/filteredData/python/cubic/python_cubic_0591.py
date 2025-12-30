import random

def main(n: int):
    # 生成测试数据：a 为长度 n 的数字串，b 为长度 n 或 n+1 的数字串
    # 为了覆盖两种分支：len(b) > len(a) 和 len(b) <= len(a)，这里随机选择
    a_len = n
    # 让 b 的长度在 [n-1, n+1] 之间波动（最小保持 1）
    b_len = max(1, a_len + random.choice([-1, 0, 1]))

    # 生成由数字字符组成的字符串
    a = ''.join(str(random.randint(0, 9)) for _ in range(a_len))
    b = ''.join(str(random.randint(0, 9)) for _ in range(b_len))

    # ===== 以下是原程序逻辑的无 input() 版本 =====

    if len(b) > len(a):
        l = [int(i) for i in a]
        l.sort()
        l = l[::-1]
        temp = [str(i) for i in l]
        s = ''.join(temp)
        print(s)
    else:
        d = {}
        for i in a:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1

        def find(i):
            if i in d and d[i] > 0:
                d[i] = d[i] - 1
                return i

            for j in range(int(i), -1, -1):
                j = str(j)
                if j in d and d[j] > 0:
                    d[j] = d[j] - 1
                    return j
            return None

        def fun(dct):
            l = []
            for k in dct:
                if dct[k] > 0:
                    l = l + [int(k)] * dct[k]
            l.sort()
            l = l[::-1]
            temp = [str(i) for i in l]
            s = ''.join(temp)
            return s

        # new 和对它的修改原先通过 global 处理，这里改为外部变量引用
        def fun2(x, new_str):
            new_local = new_str
            for i in range(x - 1, -1, -1):
                temp = new_local[i]
                for j in range(int(temp) - 1, -1, -1):
                    j = str(j)
                    if j in d and d[j] > 0:
                        new_local = new_local[:i] + j
                        d[j] = d[j] - 1
                        d[temp] = d[temp] + 1
                        return new_local
                d[temp] = d[temp] + 1
            return new_local

        flag = 0
        new = ''
        for i in range(len(b)):
            if flag == 0:
                temp = find(b[i])
                if temp is None:
                    new = fun2(i, new)
                    new = new + fun(d)
                    break
                else:
                    new = new + temp
            else:
                new = new + fun(d)
                break

        print(new)


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)