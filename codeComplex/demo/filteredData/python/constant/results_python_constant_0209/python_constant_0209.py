def main(n):
    # 根据 n 生成确定性的 k1, k2, k3
    # 映射规则：随 n 变化，覆盖各种组合情况
    k1 = (n % 5) + 1
    k2 = (n // 2 % 5) + 1
    k3 = (n // 3 % 5) + 1

    a = [k1, k2, k3]
    a = sorted(a)
    if a[0] == 1 or a.count(2) >= 2 or a.count(3) == 3:
        # print("YES")
        pass
    elif a.count(4) == 2 and a.count(2) == 1:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)