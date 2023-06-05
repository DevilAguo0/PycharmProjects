# raise NameError  #直接抛出异常
# name_error = NameError  #使用异常对象引发异常
# raise name_error


# 由异常引发异常
# try:
#     num
# except NameError as e:
#     raise


#  异常的传递
def get_width():
    print("get_width开始执行")
    num = int(input("请输入除数："))
    width_len=10/num
    print("get_width执行结束")
    return width_len
def calc_area():
    print("calc_area开始执行")
    width_len=get_width()
    print("calc_area执行结束")
    return width_len *width_len
def show_area():
    try:
        print("show_area开始执行")
        area_val = calc_area()
        print(f'正方形的面积是{area_val}')
        print("show_area执行结束")
    except ZeroDivisionError as e:
        print(f"捕获到异常：{e}")
if __name__=="__main__":
    show_area()

