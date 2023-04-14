class parent:
    def p_function(self):
        print("parent class")
class child(parent):
    def c_function(self):
        print("child claass")
obj=child()
obj.p_function()
obj.c_function()