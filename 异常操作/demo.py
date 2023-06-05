try:
    fh=open("testfile","w")
    fh.write("这是一个测试文件，用于测试异常！！")
except IOError:
    print("Error:没有找到文件或读取文件失败")
except NameError:
    print("Nameerror")
else:
    print("内容写入成功")
    fh.close()
finally:
    print("无论是是否有异常都要执行的代码！")
