def main(n):
    # 根据规模 n 生成测试数据：长度为 n 的字符串，由 'x' 和 'o' 构成
    # 这里示例：前 n//2 个为 'x'，后面为 'o'，可按需修改生成规则
    half = n // 2
    s = "x" * half + "o" * (n - half)

    ans = 0
    cnt = 0
    for x in s:
        if x == "x":
            cnt += 1
            if cnt >= 3:
                ans += 1

        else:
            cnt = 0

    # 返回或打印结果，这里选择返回
    return ans


if __name__ == "__main__":
    # 示例：调用 main(10)，不会使用 input()
    res = main(10)
    # print(res)
    pass