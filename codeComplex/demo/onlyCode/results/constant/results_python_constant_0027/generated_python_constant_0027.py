def main(n):
    # 根据 n 生成测试数据，这里假设原本的 n 就是规模本身
    g = n // 2
    return g + n


if __name__ == "__main__":
    # 示例调用：可根据需要修改或删除
    test_n = 10
    print(main(test_n))