def demo(name, gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("{}是{}".format(name, gender_text))


demo("Jihong", False)
