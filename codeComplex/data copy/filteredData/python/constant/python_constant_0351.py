def main(n):
    d = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind",
    }

    colors = ["purple", "green", "blue", "orange", "red", "yellow"]
    i = n % (len(colors) + 1)

    for x in range(i):
        color_to_pop = colors[x]
        if color_to_pop in d:
            d.pop(color_to_pop)

    # print(len(d))
    pass
    for v in d.values():
        # print(v)
        pass
if __name__ == "__main__":
    main(3)