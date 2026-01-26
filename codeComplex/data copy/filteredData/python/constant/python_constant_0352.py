def main(n):
    d = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind",
    }
    colors = list(d.keys())
    l = [colors[i % 6] for i in range(n)]
    # print(6 - n)
    pass
    for key in d:
        if key not in l:
            # print(d[key])
            pass
if __name__ == "__main__":
    main(3)