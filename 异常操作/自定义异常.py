# class CustomError(Exception):
#     pass
#
#
#
# try:
#     pass
#     raise CustomError("出现错误")
# except CustomError as  error:
#     print(error)


class FileTypeError(Exception):
    def __init__(self, err="仅支持jpg/png/bmg"):
        super(FileTypeError, self).__init__(err)


file_name = input("请输入上传照片的名称（包含格式）：")
try:
    if file_name.split(".")[1] in ["jpg", "png", "bmp"]:
        print(file_name.split("."))
        print("上传成功")
    else:
        raise FileTypeError()
except Exception as error:
    print(error)
