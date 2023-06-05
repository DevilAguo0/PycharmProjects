old_file=input("请输入您要复制的文件的路径：")
new_file=input("请输入目标路径：")
with open(old_file,"r") as student:
    student_file=student.read()
    with open(new_file,"w+") as student_copy10:
        student_copy10.write(student_file)
        print(student_copy10.read())
# with open(new_file,"r") as f:
#     print(f.read())
print("复制成功！")
