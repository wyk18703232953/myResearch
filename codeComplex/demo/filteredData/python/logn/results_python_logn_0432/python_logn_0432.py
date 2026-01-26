def main(n):
    """
    生成规模为 n 的测试数据并运行逻辑。
    测试数据约定：
      - t = n
      - 对于第 i 组：n_i = i + 1, k_i = i + 1
    """
    t = n
    for case_idx in range(t):
        ni = case_idx + 1
        ki = case_idx + 1

        if ni > 32:
            # print("YES", ni - 1)
            pass

        else:
            max_splits = (4 ** ni - 1) // 3
            if ki > max_splits or (ni, ki) == (2, 3):
                # print("NO")
                pass

            else:
                done = False
                for i in range(ni):
                    if ki < 2 ** (i + 2) - i - 3:
                        # print("YES", ni - i)
                        pass
                        done = True
                        break
                if not done:
                    # print("YES", 0)
                    pass
if __name__ == "__main__":
    # 示例运行：可根据需要修改 n 的大小
    main(10)