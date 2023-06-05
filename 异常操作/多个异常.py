try:
    # print(count)
    demo_list=["python","Java","C","C++"]
    print(demo_list[5])
except (NameError,IndexError) as Error:
    print(f"异常原因:{Error}")
# except NameError as error:
#     print(f'异常原因：{error}')
# except IndexError as error:
#     print(f'异常原因：{error}')
