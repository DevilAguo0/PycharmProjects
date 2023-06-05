stu_info = []


class Student:
    def __init__(self, name, gender, phone):
        self.name = name
        self.gender = gender
        self.phone = phone


class StudentManage(object):

    def __init__(self):
        pass

    def print_menu(self):
        print('=' * 30)
        print('学生管理系统')
        print('1.添加学生信息')
        print('2.删除学生信息')
        print('3.修改学生信息')
        print('4.显示所有学生信息')
        print('0.退出系统')

    def add_stu_info(self):
        # 提示并获取学生的姓名
        Student.name = input('请输入新学生的姓名:')
        # 提示并获取学生的性别
        Student.gender = input('请输入新学生的性别:')
        # 提示并获取学生的手机号
        Student.phone = input('请输入新学生的手机号码:')
        new_info = dict()
        new_info['name'] = Student.name
        new_info['sex'] = Student.gender
        new_info['phone'] = Student.phone
        stu_info.append(new_info)

    # 定义删除学生信息的函数
    def del_stu_info(self, stu_info):
        del_num = int(input('请输入要删除的序号：')) - 1
        if del_num in range(0, len(stu_info)):
            del stu_info[del_num]
        else:
            print('数据不存在')

    # 定义修改学生信息的函数，具体代码如下：
    def modify_stu_info(self, stu_info):
        if len(stu_info) != 0:
            stu_id = int(input('请输入要修改学生的序号:'))
            new_name = input('请输入要修改学生的姓名:')
            new_sex = input('请输入要修改学生的性别:(男/女)')
            new_phone = input('请输入要修改学生的手机号码:')
            stu_info[stu_id - 1]['name'] = new_name
            stu_info[stu_id - 1]['sex'] = new_sex
            stu_info[stu_id - 1]['phone'] = new_phone
        else:
            print('学生信息表为空')

    def main(self):
        while True:
            self.print_menu()  # 打印菜单
            key = input("请输入功能对应的数字：")  # 获取用户输入的序号
            if key == '1':  # 添加学生信息
                self.add_stu_info()
            elif key == '2':  # 删除学生信息
                self.del_stu_info(stu_info)
            elif key == '3':  # 修改学生信息
                self.modify_stu_info(stu_info)
            elif key == '4':  # 查看所有学生的信息
                self.show_stu_info(stu_info)
            elif key == '0':
                quit_confirm = input('确认退出？(Yes or No):')
                if quit_confirm == 'Yes':
                    break  # 跳出循环
                else:
                    print('输入有误，请重新输入')

    def show_stu_info(self, stu_info):
        print('学生的信息如下：')
        print('=' * 30)
        print('序号    姓名    性别    手机号码')
        i = 1
        for tempInfo in stu_info:
            print("%d    %s    %s    %s" %
                  (i, tempInfo['name'], tempInfo['sex'], tempInfo['phone']))
            i += 1


if __name__ == '__main__':
    admin = StudentManage()
    admin.main()

