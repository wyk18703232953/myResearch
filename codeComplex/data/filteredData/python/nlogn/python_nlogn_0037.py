def main(n):
    # 生成确定性的输入数组 a，规模为 n
    # 使用简单的算术构造：a[i] = (i % 5) + 1，保证元素为正整数且有重复
    a = [(i % 5) + 1 for i in range(n)]
    
    # 原始算法逻辑
    a.sort()
    if a[-1] == 1:
        ans = a[:-1] + [2]
    else:
        ans = [1] + a[:-1]
    
    print(*ans)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 进行规模化实验
    main(10)