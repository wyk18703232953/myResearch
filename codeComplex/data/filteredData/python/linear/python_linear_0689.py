import math

def f(n, k):
    if k == 1:
        return (n * (n + 1)) // 2
    a = math.floor(math.log(n, k))
    b = sum(k ** i for i in range(a + 1))
    c = sum((i + 1) * k ** i for i in range(a + 1))
    if n < b:
        return c - (b - n) * (a + 1)

    else:
        return c + (n - b) * (a + 2)

def main(n):
    # Deterministically generate s from n
    # Map n to a feasible s within the same structural constraints as original input
    # Use a simple arithmetic formula to keep it deterministic and scalable
    s = (n * (n + 1)) // 4 if n > 0 else 0

    if s == (n * (n + 1)) // 2:
        # print("Yes")
        pass
        a = [str(i + 1) for i in range(n - 1)]
        # print(" ".join(a))
        pass
    elif s > (n * (n + 1)) // 2:
        # print("No")
        pass
    elif s < 2 * n - 1:
        # print("No")
        pass

    else:
        mini = 1
        maxi = n - 1
        curr = 1
        while True:
            a_val, b_val = f(n, curr), f(n, curr + 1)
            if b_val > s:
                mini = curr + 1
                curr = math.ceil((curr + maxi) / 2)
            elif a_val <= s:
                maxi = curr - 1
                curr = (curr + mini) // 2

            else:
                opt = curr + 1
                break
        depths = [0, 1] + [0] * (n - 1)
        ins = 1
        ind = 2
        while True:
            a_count = min(opt ** (ind - 1), n - ins)
            depths[ind] = a_count
            ind += 1
            ins += a_count
            if ins == n:
                break
        b_val = f(n, opt)
        left = s - b_val
        far = ind - 1
        bulk = ind - 1
        if depths[bulk] == 1:
            bulk -= 1
        while left > 0:
            if far + 1 - bulk <= left:
                far += 1
                left -= far - bulk
                depths[far] += 1
                depths[bulk] -= 1
                if depths[bulk] == 1:
                    bulk -= 1

            else:
                depths[bulk] -= 1
                depths[bulk + left] += 1
                left = 0
        verts = [None] * far
        sumi = 0
        for i in range(far):
            verts[i] = list(range(sumi + 1, sumi + 1 + depths[i + 1]))
            sumi += depths[i + 1]
        out = ""
        for i in range(1, far):
            for j in range(len(verts[i])):
                out += str(verts[i - 1][j // opt]) + " "
        # print("Yes")
        pass
        # print(out)
        pass
if __name__ == "__main__":
    main(10)