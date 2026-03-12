class Trapezoidal_rule:
    def __init__ (self,h,listfx):
        self.h=h
        self.listfx=listfx
    def Trapezoidal_rule(self):
        sum=0
        for i in range(1,len(self.listfx)-1):
         sum+=self.listfx[i]
        sum*=2
        sum+=self.listfx[0]+self.listfx[-1]
        sum*=self.h/2
        print("The solution: ",sum)








