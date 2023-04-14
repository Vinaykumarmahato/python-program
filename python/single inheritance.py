# if one class inhetis the anothher class that is called single inheritance.
# +++++++++++++=+++++++=+++==================++++++++++++++++++++++++=======.
class parent:
    def p_fun(self):
        print("this class name is pareent class")
class child(parent):
    def c_fun(self):
        print("this class naame is child class")
obj=child()
obj.p_fun()
obj.c_fun()