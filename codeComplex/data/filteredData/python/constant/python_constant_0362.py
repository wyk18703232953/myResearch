def main(n):
    colors = ["purple", "green", "red", "blue", "orange", "yellow"]
    l = []
    for i in range(n):
        # Deterministically generate strings:
        # First fill with colors, then with non-color strings
        if i < len(colors):
            l.append(colors[i])

        else:
            l.append("str_" + str(i))
    # print(6 - n)
    pass

    if "purple" not in l:
        # print("Power")
        pass
    if "green" not in l:
        # print("Time")
        pass
    if "red" not in l:
        # print("Reality")
        pass
    if "blue" not in l:
        # print("Space")
        pass
    if "orange" not in l:
        # print("Soul")
        pass
    if "yellow" not in l:
        # print("Mind")
        pass
if __name__ == "__main__":
    main(4)