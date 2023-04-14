# multilevel inheritance: it has such type of family like grand parent , parent and child
class devpujan: # grand parent
    def de_fun(self):
        print("this is the graand parent class and the naame the grand parent class is devpujan mahto")
class vijay(devpujan): # pareent class
    def  vij_fun(self):
        print("this is the paarent class and the name of the parent class is vijay mahto")
class vinay(vijay): #  child class
    def vin_fun(self):
        print("this is the child class and the name of the class is vinay kumar")
obj=vinay()
obj.vin_fun()
obj.vij_fun()
love=vijay()
love.vij_fun()
love.de_fun()