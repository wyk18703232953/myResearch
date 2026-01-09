my_list_template = {
    "purple": "Power",
    "green": "Time",
    "blue": "Space",
    "orange": "Soul",
    "yellow": "Mind",
    "red": "Reality",
}

def main(n):
    my_list = dict(my_list_template)
    colors = list(my_list.keys())
    for i in range(min(n, len(colors))):
        my_list.pop(colors[i])
    # print(len(my_list))
    pass
    for key in my_list:
        # print(my_list[key])
        pass
if __name__ == "__main__":
    main(3)