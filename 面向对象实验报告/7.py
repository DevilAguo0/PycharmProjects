class Nstr:
    def __init__(self, arg):
       self.x=arg
    def __sub__(self,other):
        c=self.x.replace(other.x,"")
        return c
m=Nstr("asdffasdf")
n=Nstr("asd")
print(m-n)
