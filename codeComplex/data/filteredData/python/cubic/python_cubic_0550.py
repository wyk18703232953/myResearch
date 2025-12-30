import random

def main(n):
    # 生成测试数据：长度为 n 的 s1，长度为 m 的 s2（1 <= m <= n）
    # 数字串，只包含 '0'~'9'
    if n <= 0:
        return
    # 随机生成 s1，确保不全是前导 0
    s1 = ''.join(str(random.randint(0, 9)) for _ in range(n))
    # 为了避免 int 转换时的歧义，可以去掉前导零再保证至少是 '0'
    s1 = s1.lstrip('0') or '0'
    # 随机生成 s2，长度在 1 到 n 之间
    m = random.randint(1, n)
    s2 = ''.join(str(random.randint(0, 9)) for _ in range(m))
    s2 = s2.lstrip('0') or '0'

    # 以下是原逻辑，去掉 input() 并用生成的 s1, s2
    arr = list(s1)
    arr.sort(reverse=True)

    if len(s2) > len(s1):
        t = ""
        for i in arr:
            t += i
        print(t)
    else:
        t = ""
        l = len(s1)
        for _ in range(l):
            index = -1
            ma = -1
            for j in range(len(arr)):
                temp = arr[j]
                tt = []
                for k in range(len(arr)):
                    if k != j:
                        tt.append(arr[k])
                tt.sort()
                for k in tt:
                    temp += k
                temp = t + temp
                if int(s2) >= int(temp):
                    if int(arr[j]) > ma:
                        ma = int(arr[j])
                        index = j
            t += arr[index]
            del arr[index]
        print(t)


# 示例：直接调用 main
if __name__ == "__main__":
    main(5)