def main(n):
    # Generate a deterministic binary string of length n
    s = ''.join('1' if i % 2 == 0 else '0' for i in range(n))

    if "0" in s:
        if "1" in s:
            # print("1" + "0" * s.count("0"))
            pass

        else:
            # print("0")
            pass

    else:
        # print("1")
        pass
if __name__ == "__main__":
    main(10)