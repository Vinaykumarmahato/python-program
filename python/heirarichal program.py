class parent:
    def p_fun(self):
        print("this is parent class")
class child1(parent):
    def c1_fun(self):
        print("this is the first son of the parent class")
class child2(parent):
    def c2_fun(self):
        print("this is the second child of the parent class")
class child3(parent):
    def c3_(self):
        print(" this is the third child of the parent class")
obj=child3()
obj.p_fun()
obj.c3_()
obj=child2()
obj.p_fun()
obj.c2_fun()
obj=child1()
obj.p_fun()
obj.c1_fun()