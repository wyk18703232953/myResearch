def main(n):
    # 生成长度为 n 的数组 a，元素为确定性的整数模式
    # a[i] = (i * 2) % (max(1, n//3 + 1)) 保证有重复和一定分布
    if n <= 0:
        # print("NO")
        pass
        return
    mod_base = max(1, n // 3 + 1)
    a = [(i * 2) % mod_base for i in range(n)]

    l = list(set(a))
    l.sort()
    if len(l) >= 2:
        # print(l[1])
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)