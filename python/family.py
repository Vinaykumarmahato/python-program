class devpujan:
    def d_fun(self):
        print("the name is devpujan mahto")
class vijay(devpujan):
    def vij_fun(self):
        print("devpujan mahto is the father of vijay mahto")
class vinay(devpujan):
    def vi_fun(self):
        print("vijay mahto is the father of vinay kumar")
obj=vijay()
obj.d_fun()
obj.vij_fun()
obj=vinay()
obj.d_fun()
obj.vi_fun()