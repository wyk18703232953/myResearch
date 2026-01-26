from math import sin, pi

def main(n):
    # 根据 n 生成测试数据，这里令 r = n，用户可按需修改生成规则
    r = n
    result = r * sin(pi / n) / (1 - sin(pi / n))
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 的取值进行测试
    main(6)