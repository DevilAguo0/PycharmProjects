import threading
import os


def copy_file(file_name, source_dir, dest_dir):
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name
    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    source_dir = "windows7"
    dest_dir = "/Users/wevilaguo/Desktop/Demo"
    try:
        os.mkdir(dest_dir)
    except Exception as result:
        print(result)
        print("文件夹已存在")
    source_list = os.listdir(source_dir)
    for file_name in source_list:
        copy_proess = threading.Thread(target=copy_file, args=(file_name,
                                                               source_dir, dest_dir))
        copy_proess.start()
    else:
        print("复制完成！")
