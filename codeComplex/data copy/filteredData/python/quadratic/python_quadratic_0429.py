def main(n):
    # n 表示序列长度
    if n <= 0:
        return

    # 确定性生成长度为 n 的 0/1 序列
    # 模式：arr[i] = (i * 7 + 3) % 2
    arr = [(i * 7 + 3) % 2 for i in range(n)]

    if len(set(arr)) == 1:
        # print('YES')
        pass

    else:
        val = sum(arr)
        factor = set()
        for i in range(1, int(val ** 0.5) + 1):
            if val % i == 0:
                factor.add(i)
                factor.add(val // i)
        can = False
        for i in factor:
            each = val // i
            if 1 < i <= n:
                idx = 0
                temp = 0
                cnt = 0
                while idx < n:
                    if temp + arr[idx] < each:
                        temp += arr[idx]
                    elif temp + arr[idx] > each:
                        temp = 0

                    else:
                        temp = 0
                        cnt += 1
                    idx += 1
                if cnt == i:
                    can = True
        # print('YES' if can else 'NO')
        pass
if __name__ == "__main__":
    # 示例：使用 n = 20 作为输入规模
    main(20)