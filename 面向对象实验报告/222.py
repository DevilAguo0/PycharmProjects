a_list = [1, 2, 3, 4, 5, 6, 7]




class Mylist(list):
    def __init__(self,a_list):
        super(Mylist, self).__init__()

    def mul(self):
        result = 1
        for i in a_list:
            result *= i
        return result


mylist = Mylist(a_list)
print(mylist.mul())
