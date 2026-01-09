class APaintTheNumbers:
    def solve(self, n, a):
        a.sort()
        ans = 0
        done = [0] * n
        for i in range(n):
            if done[i]:
                continue
            ans += 1
            for j in range(i, n):
                if done[j]:
                    continue
                if a[j] % a[i] == 0:
                    done[j] = 1
        return ans


def main(n):
    # 生成测试数据：1 到 n 的整数
    a = list(range(1, n + 1))

    solver = APaintTheNumbers()
    ans = solver.solve(n, a)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：规模为 10
    main(10)