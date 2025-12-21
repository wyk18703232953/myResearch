def main(n):
    t = n
    results = []
    for _ in range(t):
        cur_n = n
        k = n
        if cur_n > 32:
            results.append(("YES", cur_n - 1))
        else:
            max_splits = (4 ** cur_n - 1) // 3
            if k > max_splits or (cur_n, k) == (2, 3):
                results.append(("NO",))
            else:
                done = False
                for i in range(cur_n):
                    if k < 2 ** (i + 2) - i - 3:
                        results.append(("YES", cur_n - i))
                        done = True
                        break
                if not done:
                    results.append(("YES", 0))
    return results

if __name__ == "__main__":
    print(main(5))