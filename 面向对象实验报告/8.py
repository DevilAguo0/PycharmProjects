# 实现一个简单的书籍出租管理系统（面向对象）
# 实现功能：
# 1. 添加书籍
# 2. 删除书籍
# 3. 修改书籍
# 4. 查询书籍
# 5. 查询所有书籍
# 6. 退出系统


# 定义一个类，类名为Book
# 定义一个方法，方法名为__init__，方法的参数为name, author, price, count
# 定义一个方法，方法名为__str__，方法的返回值为书名，作者，价格，数量
# 实例化一个对象，对象的名称为book
# 调用对象的方法，输出对象的信息
# 定义一个类，类名为BookManager
# 定义一个方法，方法名为add_book，方法的参数为book
# 定义一个方法，方法名为del_book，方法的参数为name
# 定义一个方法，方法名为mod_book，方法的参数为name, author, price, count
# 定义一个方法，方法名为find_book，方法的参数为name
# 定义一个方法，方法名为find_all，方法的返回值为所有书籍信息
# 定义一个方法，方法名为exit，方法的返回值为退出系统
# 实例化一个对象，对象的名称为book_manager
# 调用对象的方法，输出对象的信息
class Book:
    def __init__(self, name, author, price, count):
        self.name = name
        self.author = author
        self.price = price
        self.count = count

    def __str__(self):
        return '书名：%s\n作者：%s\n价格：%s\n数量：%s' % (self.name, self.author, self.price, self.count)


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def del_book(self, name):
        for book in self.books:
            if book.name == name:
                self.books.remove(book)
                break

    def mod_book(self, name, author, price, count):
        for book in self.books:
            if book.name == name:
                book.author = author
                book.price = price
                book.count = count
                break

    def find_book(self, name):
        for book in self.books:
            if book.name == name:
                print(book)
                break

    def find_all(self):
        for book in self.books:
            print(book)

    def exit(self):
        print('退出系统')


book = Book('python', 'zhangsan', 100, 10)
book_manager = BookManager()
book_manager.add_book(book)
book_manager.find_book('python')
book_manager.find_all()
book_manager.exit()
