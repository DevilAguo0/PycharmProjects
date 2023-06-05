try:
    file = open('demo.txt',"r+")
    file.write('人生苦短，我用python')
except Exception as error:
    print("文件写入失败",error)
finally:
    file.close()
    print("文件关闭")



