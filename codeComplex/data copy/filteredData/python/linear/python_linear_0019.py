def main(n):
    # Generate a deterministic list of n integers where exactly one element
    # has parity different from all the others.
    if n <= 1:
        s = [1]

    else:
        # Make all elements even
        s = [2 * (i + 1) for i in range(n)]
        # Make the last element odd so it is the unique one
        s[-1] = s[-1] + 1

    odd, even, oddIndex, evenIndex = 0, 0, 0, 0
    counter = 0
    for i in s:
        if i % 2 == 0:
            even += 1
            evenIndex = counter

        else:
            odd += 1
            oddIndex = counter
        counter += 1
    ans = evenIndex + 1 if even == 1 else oddIndex + 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)