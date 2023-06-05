def copy_file(oldfile, newfile):
    oldfile = open(oldfile, "r")
    newfile = open(newfile, "w")
    while True:
        file_content = oldfile.read(50)
        if file_content == 0:
            break
        newfile.write(file_content)
    oldfile.close()
    newfile.close()
    return


copy_file("/Users/wevilaguo/Desktop/studentmanage.py", "/Users/wevilaguo/Desktop/last.py")
