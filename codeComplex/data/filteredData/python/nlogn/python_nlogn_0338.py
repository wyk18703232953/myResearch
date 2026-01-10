def main(n):
    # 生成确定性的字符串列表，长度为 n
    # 构造方式：第 i 个字符串为从 'a' 开始的 (i % 26 + 1) 个相同字符
    # 这样字符串长度随 i 增大，适合触发排序和包含关系检查
    ar = []
    for i in range(n):
        length = i % 26 + 1
        ch = chr(ord('a') + (i % 26))
        ar.append(ch * length)

    sortedAr = sorted(ar, key=len)
    flag = False
    for i in range(n - 1):
        if sortedAr[i + 1].find(sortedAr[i]) == -1:
            print('NO')
            flag = True
            break
    if not flag:
        print('YES')
        for s in sortedAr:
            print(s)


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 规模做时间复杂度实验
    main(10)