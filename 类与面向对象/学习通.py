# class Test:
#     count = 21
#     def print_num(self):
#         count=20
#         self.count+=20
#         print(count,self.count)
# test=Test()
# test.print_num()
class T:
    def __init__(self):
        self.w = 100
        self.h = 100

    def __init__(self, w, h):
        self.w = w
        self.h = h


t1 = T()
t2 = T(10, 10)
print(t1.w, t2.w)
