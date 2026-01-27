def main(n):
    # n is unused in the original logic; we just need a deterministic input string.
    # Use n to generate a simple deterministic string so complexity can scale.
    s = "".join(chr(ord('a') + (i % 26)) for i in range(max(1, n)))
    # print(0, 0, s)
    pass
if __name__ == "__main__":
    main(5)