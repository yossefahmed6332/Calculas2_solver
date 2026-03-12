import sympy  as sp
import Trapezoidal 
from Rectangular import Rectangular_rule
from simpson import Simpson
from Trapezoidal import Trapezoidal_rule

def Createlistfx(h,lowerLimit,upperLimit,fun,x):
    listfx=[]
    i=lowerLimit
    while(i<=upperLimit):
        fx = fun.subs(x, i).evalf()
        print(fx)
        fx=float(fx)
        listfx.append(fx)
        i+=h
    return listfx









x = sp.symbols('x')
print("Hello project ")
while(True):
    print("choose 1 if you want to close program , choose 2 to continue")
    choice=int(input())
    if(choice==1):
        break
    #prepare variables 
    fun=sp.sympify(input("Enter function, use x as variable"))
    lowerLimit=float(input("Enter lower limit"))
    upperLimit=float(input("Enter upper limit"))
    n=int(input("Enter n"))
    h=(upperLimit-lowerLimit)/n


    listfx=Createlistfx(h,lowerLimit,upperLimit,fun,x)
    #evaluate integration 
    integration=sp.Integral(fun,(x,lowerLimit,upperLimit))
    #Create 2 list , x and f(x)

        
    #user choose rule 
    choice=int(input("Choose 1 for trapezpodal , choose 2 to rectangular and choose 3 to simpson and for all enter 4"))
    if choice==1: 
      T=Trapezoidal_rule(h,listfx)
      T.Trapezoidal_rule()
    elif choice==2:
        R=Rectangular_rule(h,listfx)
        R.Rectangular_rule()
    elif choice==3:
        if not n%2 ==0 :
            print("needed a even number of intervals")
            continue
        S=Simpson(h,listfx)
        S.Simpson_rule()

    elif choice==4:
         print("Trapezoidal rule: ")
         T=Trapezoidal_rule(h,listfx)
         T.Trapezoidal_rule()
         print("Simpson rule: ")
         S=Simpson(h,listfx)
         S.Simpson_rule()
         print("Rectangular rule: ")
         R=Rectangular_rule(h,listfx)
         R.Rectangular_rule()



    else:
        print("Wrong input , try again")

print("It is finished , Thanks for using my program")