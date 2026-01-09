def main(n):
    # Deterministic data generation:
    # We simulate a tree-like parent array l of size n+1 (1-based),
    # where for i in [2..n], l[i] = i//2 (a fixed structure, e.g., a binary heap parent relation).
    # Then we follow the original algorithm on this generated structure.

    d = [0] * (n + 1)
    l = [0, 0]  # l[0] unused, l[1] = 0 as in original code
    m = [0] * (n + 1)
    a = 0

    # original: for _ in range(n-1): a=int(input()); l.append(a); m[a]+=1
    # here: deterministically generate a parent for nodes 2..n
    for i in range(2, n + 1):
        a = i // 2
        l.append(a)
        m[a] += 1

    # original: for i in range(1,n+1): if m[i]==0: d[l[i]]+=1
    for i in range(1, n + 1):
        if m[i] == 0:
            d[l[i]] += 1

    # original: for i in range(1,n+1): if m[i]>0 and d[i]<3: print("No"); break; else: print("Yes")
    for i in range(1, n + 1):
        if m[i] > 0 and d[i] < 3:
            # print("No")
            pass
            break

    else:
        # print("Yes")
        pass
if __name__ == "__main__":
    main(10)