class grandparent:
    def g_fun(self):
        print("this is the grand parent class")
class parent(grandparent):
    def p_fun(self):
        print("this is the paarent class ")
class child(parent):
    def c_fun(self):
        print("this is the child class")
object=child()
object.c_fun()
object.p_fun()
object.g_fun()