# it enable one derived class to inherits properties from more than one base class
class rajnath:  # rajnaath iss first faather of the child
    def raa_fun(self):
        print("rajnath is the father of rajnish kumar")
class pundev:   # pundev is the father of rajnish kumar
    def pu_fun(self):
        print("pundev is the father of rajnish kumar ")
class rajveer:  # raajveer is the father of rajnish kumar 
    def raj_fun(self):
        print("rajnath is the father of rajnish kumar")
class  vivek:  # vivek is the father of rajnish kumar
    def viv_fun(self):
        print("rajnath is the father of mr vivek kumar")
        
class rajnish(rajnath,pundev,rajveer,vivek):
    def rau_fun(self):
        print("rajnish kumar is the child of rajnath , pundev, rajveer and vivek")
        
obj=rajnish()
obj.rau_fun()
obj.pu_fun()
obj.raa_fun()
obj.raj_fun()
obj.viv_fun()
