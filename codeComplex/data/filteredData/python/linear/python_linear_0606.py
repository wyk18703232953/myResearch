import random

def main(n: int):
    # 生成规模为 n 的测试数据（本题中 n 直接作为规模使用）
    # 如需随机测试，可在此处对 n 进行随机化或生成其他辅助数据

    ans = [(0, 0)]
    for i in range(1, n):
        ans.append((0, i))
        ans.append((i, 0))
        ans.append((0, -i))
        ans.append((-i, 0))

    for i in range(n):
        print(f"{ans[i][0]} {ans[i][1]}")

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可修改 n 的值
    main(10)