class parent:
    def p_fun(self):
        print(" this class is known as parent class")
class child(parent):
    def c_fun(self):
        print(" this class is known as child class")
obj=child()
obj.c_fun()
obj.p_fun()