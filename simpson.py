class Simpson:
    def __init__ (self,h,listfx):
        self.h=h
        self.listfx=listfx

    def Simpson_rule(self):
     sum1=0#get frist term
     for i in range(2,len(self.listfx)-2,2):
        sum1+=self.listfx[i]
     sum1*=2

     sum2=0#get second term
     for i in range(1,len(self.listfx),2):
         sum2+=self.listfx[i]
       
     sum2*=4
     sum=0
     sum+=(self.listfx[0]+self.listfx[len(self.listfx)-1])
     sum+=sum1+sum2
     sum*=self.h/3
     print(sum)


