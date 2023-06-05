ticket = True
knife_long = 40
if ticket:
    print("☣︎检票已通过，下一步请进行安检")
    if knife_long >= 30:
        print("〄危险危险，您带的刀的长度为{}".format(knife_long))
    else:
        print("安检已通过")
else:
    print("大哥，请先买票")
