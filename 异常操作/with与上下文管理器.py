class OPenOperation:
    def __init__(self, path, mode):
        self.__path = path
        self.__mode = mode
        # 记录要操作的文件路径和模式

    def __enter__(self):
        print('代码执行到__enter__')
        self.__handle = open(self.__path, self.__mode)
        return self.__handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('代码执行到__exit__')
        self.__handle.close()


with OPenOperation('自定义上下文管理.txt', "a+") as file:
    # 创建写入文件
    file.write("Custom context Manage")
    print('文件写入成功')
