def main(n):
    # Generate deterministic input of size n
    a = n
    z = [i * 2 + 1 for i in range(a)]
    ans = []
    k = len(z)
    for i in range(len(z)):
        if (z[i] - i) % len(z) == 0:
            ans.append((z[i] - i) // k)

        else:
            ans.append((z[i] - i) // k)
            ans[-1] += 1
    t = min(ans)
    result = ans.index(t) + 1
    return result


if __name__ == "__main__":
    # print(main(10))
    pass