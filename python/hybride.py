class parent1:
    def p1_fun(self):
        print("this is the first parent class")
class parent2:
    def p2_fun(self):
        print("this is the second parent class")
class child(parent1,parent2):
    def c_fun(self):
        print("this is the son of two parent ,it means the son of parent 1 and the son of parent second")
object=child()
object.p1_fun()
object.p2_fun()
object.c_fun()