def main(n):
    # 生成长度为 n 的测试数据串 s（只包含数字字符）
    # 这里给一个简单示例：前 n-1 位为 '1'，最后一位为 '0'，可按需要自定义生成策略
    if n <= 0:
        return 'NO'
    s = '1' * max(0, n - 1) + '0'

    # 以下为原逻辑的封装与改写（去掉 input）
    a = []
    for v in s:
        if v != '0' and v != '\n':
            a.append(v)

    if not a and n > 1:
        return 'YES'

    n2 = len(a)
    s2 = a
    total = 0

    for i in range(n2 - 1):
        total += int(s2[i])
        j = i + 1
        check = 1
        while j < n2:
            temp = int(s2[j])
            j += 1
            while j < n2:
                if temp >= total:
                    break
                temp += int(s2[j])
                j += 1
            if total != temp:
                check = 1
                break
        if total != temp:
            check = 0
        if check:
            return 'YES'
    return 'NO'


# 简单示例调用（调试时使用，正式使用时可删除或注释）
if __name__ == "__main__":
    print(main(5))