num=input("请输入每页小是多少条数据：")
try:
    page_size= int(num)
except Exception as e:
    page_size=20
    print(f"当前页显示{page_size}条数据")
else:
    print(f"当前页显示{num}条数据")
