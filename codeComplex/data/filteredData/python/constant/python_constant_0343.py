import random

def main(n: int) -> None:
    # 生成测试数据：此处直接使用参数 n 作为待处理的数据
    # 若需要批量测试，可自行在外部循环调用 main()
    
    if n == 0:
        print(0)
    elif n % 2 == 1:
        print((n + 1) // 2)
    else:
        print(n + 1)


# 示例：如需批量测试，可取消下面注释
# if __name__ == "__main__":
#     for _ in range(5):
#         n_test = random.randint(0, 100)
#         print(f"n = {n_test} -> ", end="")
#         main(n_test)