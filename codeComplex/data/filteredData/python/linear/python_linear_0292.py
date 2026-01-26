def main(n):
    # n 表示数组长度规模
    # 生成一个确定性的数组：包含从 0 到 n-1 的整数，其中每个数出现一次
    # 为了保证有去重效果，同时不改变题目逻辑
    a_list = [i for i in range(n)]
    a = set(a_list)
    ans = len(a) - 1 if 0 in a else len(a)
    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次确定性运行
    main(10)