def main(n: int) -> int:
    # 根据 n 生成测试数据，这里示例为 1..n 的列表
    # 可按需修改为其他生成方式
    a = list(range(1, n + 1))

    ans = 0
    # 使用副本进行操作，避免修改原始数据
    b = a[:]

    while len(b) > 0:
        c = b.pop(0)          # 取出第一个元素
        i = b.index(c)        # 在剩余列表中找到相同值的位置
        ans += i              # 累加索引
        del b[i]              # 删除该位置元素

    return ans


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时按需调用 main(n)
    result = main(5)
    print(result)