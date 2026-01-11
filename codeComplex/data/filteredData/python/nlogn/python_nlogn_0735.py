def main(n):
    # Generate deterministic test data:
    # Original input: n, then a list ai of length n
    # Here we map n to length of ai and construct ai deterministically.
    # Example construction: ai[i] = i // 2 to include some duplicates for larger n.
    ai = [i // 2 for i in range(n)]
    ai.sort()
    num = 0
    num2 = 0
    for i in range(1, n):
        if ai[i - 1] == ai[i]:
            num += 1
            num2 = i
    if num == 0:
        num3 = sum(ai)
        num4 = n * (n - 1) // 2
        ans = (num3 - num4) % 2
        if ans == 1:
            # print("sjfnb")
            pass

        else:
            # print("cslnb")
            pass
    elif num == 1:
        if (num2 > 1 and ai[num2 - 2] == ai[num2] - 1) or ai[num2] == 0:
            # print("cslnb")
            pass

        else:
            num3 = sum(ai)
            num4 = n * (n - 1) // 2
            ans = (num3 - num4) % 2
            if ans == 1:
                # print("sjfnb")
                pass

            else:
                # print("cslnb")
                pass

    else:
        # print("cslnb")
        pass
if __name__ == "__main__":
    main(10)