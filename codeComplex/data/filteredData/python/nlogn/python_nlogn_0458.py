def main(n):
    k = max(1, n // 2)
    arr = [(i * 3 + 7) % (n + 5) for i in range(n)]
    ans = arr.copy()
    ans.sort(reverse=True)
    ans = ans[:k]
    c = k
    total_sum = sum(ans)
    segments = []
    j = 0
    ans_multiset = {}
    for v in ans:
        ans_multiset[v] = ans_multiset.get(v, 0) + 1
    for i in range(n):
        if c != 1 and ans_multiset.get(arr[i], 0) > 0:
            segments.append(i + 1 - j)
            j = i + 1
            ans_multiset[arr[i]] -= 1
            if ans_multiset[arr[i]] == 0:
                del ans_multiset[arr[i]]
            c -= 1
        if c == 1:
            segments.append(n - j)
            break
    print(total_sum)
    if segments:
        print(" ".join(map(str, segments)))
    else:
        print()

if __name__ == "__main__":
    main(10)