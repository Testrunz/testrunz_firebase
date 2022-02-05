import json
import math

class PHY:
    def __init__(self, arg):
        self.arg = arg
    def VB_Mag(self):
        argument = self.arg[0:]
        def CR_l(x,y):
            ans = x+(y*0.01)
            return ans
        def CR_b(x,y):
            return x*(y*0.01)
        def TP1(x):
            return x/5
        def TP2(x):
            return x/10
        def TP3(x):
            return x/30
        def l2(x):
            return x**2
        def b2(x):
            return x**2
        CR1 = CR_l(float(argument[3]),float(argument[4]))
        CR2 = CR_l(float(argument[5]),float(argument[6]))
        CR3 = CR_l(float(argument[7]),float(argument[8]))
        CR4 = CR_l(float(argument[9]),float(argument[10]))
        CR5 = CR_l(float(argument[11]),float(argument[12]))
        CR_Mean = round((CR1+CR2+CR3+CR4+CR5)/5,2)
        OR1=CR_l(float(argument[15]),float(argument[16]))
        OR2=CR_l(float(argument[17]),float(argument[18]))
        OR3=CR_l(float(argument[19]),float(argument[20]))
        OR4=CR_l(float(argument[21]),float(argument[22]))
        OR5=CR_l(float(argument[23]),float(argument[24]))
        CRb1= CR_b(OR1,(float(argument[14])))
        CRb2= CR_b(OR1,(float(argument[14])))
        CRb3= CR_b(OR1,(float(argument[14])))
        CRb4= CR_b(OR1,(float(argument[14])))
        CRb5= CR_b(OR1,(float(argument[14])))
        CRb_Mean = round((CRb1+CRb2+CRb3+CRb4+CRb5)/5,2)
        T1= TP1(float(argument[26]))
        T2= TP2(float(argument[27]))
        T3= TP3(float(argument[28]))
        T4= TP1(float(argument[29]))
        T5= TP1(float(argument[30]))
        T6= TP1(float(argument[31]))
        Mean_T1 = round((T1+T2+T3)/3,2)
        Mean_T2 = round((T4+T5+T6)/3,2)
        Mean_T= round((Mean_T1+Mean_T2)/2,2)
        length=l2(CR_Mean)
        breadth=b2(CRb_Mean)    
        Inertia = round((float(argument[25])*(length+breadth))/12,3)
        T= round(Mean_T **2,2)      
        Mh= round((39.43 * Inertia)/T,2)
        m=round(Mh/2*CR_Mean,3)
        # print(json.dumps({"ans":"ans"}))
        print(json.dumps({"Result":[{"Vibrational Magnetometer":"Length of the bar magnet ","Mean(length)" : str(CR_Mean),"Mean(breadth)":str(CRb_Mean),"Time period of oscillator":str(Mean_T),"Inertia":str(Inertia),"The magnetic moment of the given bar magnet(Mh)":str(Mh)}]}))
