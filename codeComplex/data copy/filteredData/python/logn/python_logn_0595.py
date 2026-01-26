def solve(moves, candies_end):
    low = 0
    high = moves
    while low <= high:
        mid = (low + high) // 2
        val = ((moves - mid) * (moves - mid + 1)) // 2 - mid
        if val == candies_end:
            return mid
        elif val < candies_end:
            high = mid - 1

        else:
            low = mid + 1
    return None  # 若无解，返回 None

def main(n):
    # 根据规模 n 生成测试数据
    # 这里将 moves 设为 n
    moves = n
    # candies_end 的最大可能值是 mid=0 时的值：moves*(moves+1)//2
    max_candies = moves * (moves + 1) // 2

    # 简单测试数据：取一个中间值作为 candies_end
    # 为保证存在解，这里反向构造：选一个 mid0，然后计算对应的 candies_end
    mid0 = n // 2
    candies_end = ((moves - mid0) * (moves - mid0 + 1)) // 2 - mid0

    ans = solve(moves, candies_end)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可在外部按需调用 main(n)
    main(10)