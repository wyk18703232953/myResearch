def main(n):
    li1 = []
    li2 = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind",
    }
    colors = list(li2.keys())
    for i in range(n):
        li1.append(colors[i % 6])
    # print(6 - n)
    pass
    for key in li2:
        if key in li1:
            continue

        else:
            li1.append(key)
            # print(li2[key])
            pass
if __name__ == "__main__":
    main(3)