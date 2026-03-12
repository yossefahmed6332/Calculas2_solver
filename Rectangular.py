class Rectangular_rule:
    def __init__ (self,h,listfx):
        self.h=h
        self.listfx=listfx

    def Rectangular_rule(self): 
             print("Left Hand Rule:")
             left_sum = 0
             for i in range(len(self.listfx) - 1):
               left_sum += self.listfx[i]
             left_sum *= self.h
             print("The solution:", left_sum)

             print("Right Hand Rule:")
             right_sum = 0
             for i in range(1, len(self.listfx)):
               right_sum += self.listfx[i]
             right_sum *= self.h
             print("The solution:", right_sum)

