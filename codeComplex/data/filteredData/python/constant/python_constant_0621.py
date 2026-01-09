def main(n):
    # n 作为查询数量 Q
    Q = n
    ans = []
    # 构造 Q 组 (l, r)，满足 l <= r，且有足够变化
    # 使用确定性构造：l = i，r = i + (i % 5) + 1
    for i in range(Q):
        l = i
        r = i + (i % 5) + 1
        if l % 2 == 0 and r % 2 == 0:
            ans.append((r - l) // 2 + l)
        elif l % 2 == 1 and r % 2 == 0:
            ans.append((r - l + 1) // 2)
        elif l % 2 == 1 and r % 2 == 1:
            ans.append(0 - (r - l) // 2 - l)

        else:
            ans.append(0 - (r - l + 1) // 2)
    # print('\n'.join(map(str, ans)))
    pass
if __name__ == "__main__":
    main(10)