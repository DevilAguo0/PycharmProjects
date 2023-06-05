class StudentManage(object):
    def __init__(self, name, age, stu_num,tel):
        self.name = name
        self.age = age
        self.stu_num = stu_num
        self.tel=tel


    def print_menu(self):
        print('=' * 30)
        print('学生管理系统')
        print('1.添加学生信息')
        print('2.删除学生信息')
        print('3.修改学生信息')
        print('4.显示所有学生信息')
        print('0.退出系统')

    # 定义一个添加学生信息的函数
    def add_stu_info(self):
        # 提示并获取学生的姓名
        new_name = input('请输入新学生的姓名:')
        # 提示并获取学生的性别
        new_sex = input('请输入新学生的性别:')
        # 提示并获取学生的手机号
        new_phone = input('请输入新学生的手机号码:')
        new_info = dict()
        new_info['name'] = new_name
        new_info['sex'] = new_sex
        new_info['phone'] = new_phone
        stu_info.append(new_info)

    # 定义删除学生信息的函数
    def del_stu_info(student):
        del_num = int(input('请输入要删除的序号：')) - 1
        if del_num in range(0, len(student)):
            del student[del_num]
        else:
            print('数据不存在')

    # 定义修改学生信息的函数，具体代码如下：
    def modify_stu_info(self):
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

    # 定义显示学生信息的函数
    def show_stu_info():
        print('学生的信息如下：')
        print('=' * 30)
        print('序号    姓名    性别    手机号码')
        i = 1
        for tempInfo in stu_info:
            print("%d    %s    %s    %s" %
                  (i, tempInfo['name'], tempInfo['sex'], tempInfo['phone']))
            i += 1
