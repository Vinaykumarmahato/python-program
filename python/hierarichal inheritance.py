# hierarichal inheritance:- it enable more than one derived class  to inherits properties from a parent class

class vijaymahto: # father
    def p_fun(self):
        print("this is father of the given child name")
class vinay(vijaymahto):  # son of vijay mahto
    def vin_fun(self):
        print("this iss the son of mr. vijay mahto and the name of this boy is Er. vinay kumar mahto")
class  raja(vijaymahto): # son of vijay mahto
    def r_fun(self):
        print("this is the son of mr vijay mahto and the name of this son is raja kumar")
class lakshami(vijaymahto):
    def la_fun(self): # doughter of mr vijay mahto
        print("this is the doughter of mr vijay mahto aand the name of this doughter  is lakshami kumari") 
class garima(vijaymahto): # doughter of mr vijay mahto
    def ga_fun(self):
        print("this is the doughter of mr vijaay mahto the name of this doughter is garima devi")
class sandhaya(vijaymahto): # doughter of mr vijaay mahto
    def s_fun(self):
        print("this iss the doughter of mr vijay mahto and the namme of this doughter is sandhaya kumari")

obj=sandhaya()
obj.p_fun()
obj.s_fun()
vks=garima()
vks.p_fun()
vks.ga_fun()
love=lakshami()
love.p_fun()
love.la_fun()
rdx=raja()
rdx.p_fun()
rdx.r_fun()
ak47=vinay()
ak47.p_fun()
ak47.vin_fun()    