def main(n):
    # 映射 n 为字符串长度和 k 值
    length = max(1, n)
    k = max(1, n // 2)

    # 确定性生成长度为 length 的小写字母字符串
    # 使用循环 'a' 到 'z'
    s = ''.join(chr(97 + (i % 26)) for i in range(length))

    def tonny(i):
        return ord(i) - 96

    a = sorted(s)
    a = list(map(tonny, a))
    a = sorted(list(set(a)))
    if not a:
        # print(-1)
        pass
        return
    ans = [a.pop(0)]
    k -= 1
    for j in a:
        if j - ans[-1] > 1 and k > 0:
            k -= 1
            ans.append(j)
        if k == 0:
            break
    if k != 0:
        # print(-1)
        pass

    else:
        # print(sum(ans))
        pass
if __name__ == "__main__":
    main(10)