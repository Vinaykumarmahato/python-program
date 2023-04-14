# single inheritance
class parent:
    def p1(self):
        print("this is parent class")
class child(parent):
    def c(self):
        print("this is child class")

obj=child()
obj.p1()
obj.c()

print()
print()
# multiple inheritance

'''class parent:
    def p1_fun(self):
        print("parent class")
class father:
    def f(self):
        print("father house")
class mother:
    def m(self):
        print("mother house")
ob=mother()
ob.m() '''
# multilevel inheritance
class vijay:
    def vi_fun(self):
        print("vijay mahto")
class vinay(vijay):
    def vina_fun(self):
        print("vinay kumar mahto")
class sanjna(vinay):
    def san_fun(self):
        print("sanjna kumari ")
class raja(sanjna):
    def ra_self(self):
        print("raja kumar")
obj=raja()
obj.ra_self()
obj.san_fun()
obj.vi_fun()
obj.vina_fun()

print()
print()
# hierarichal inheritance

class vijay:
    def vij_fun(self):
        print("father of vinay kumar")
class raja(vijay):
    def taj_fun(self):
        print("son of mr vijay mahto")
class vinay(vijay):
    def vin_fin(self):
        print("son of mr vijay mahto but vinay is big son of mr vijay mahto")
o=vinay()
o.vij_fun()
o.vin_fin()
print()
print()

#  hybrid inheritance
class parent1:
    def p1_fun(self):
        print("first parent of child")
class parent2:
    def p2_fun(self):
        print("send parent of the child")
class child(parent1,parent2):
    def c_fun(self):
        print("this child if belonging from two father")
        
d=child()
d.p1_fun()
d.p2_fun()
d.c_fun()

