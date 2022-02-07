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
            return x+(y*0.01)
        def TP1(x):
            return x/5
        def TP2(x):
            return x/10
        def TP3(x):
            return (x*10)/30
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
        T1= round(TP1(float(argument[26])),2)
        T2= round(TP2(float(argument[27])),2)
        T3= round(TP3(float(argument[28])),2)
        T4= round(TP1(float(argument[29])),2)
        T5= round(TP2(float(argument[30])),2)
        T6= round(TP3(float(argument[31])),2)
        Mean_T1 = round((T1+T2+T3)/3,2)
        Mean_T2 = round((T4+T5+T6)/3,2)
        Mean_T= round((Mean_T1+Mean_T2)/2,2)
        length=round((l2(CR_Mean))/10,2)
        breadth=round((b2(CRb_Mean))/100,2)
        lb=round((length+breadth)/12,3)
        lb_n= lb*10
        Inertia = round(((float(argument[25]))*lb_n)*10,3)
        T= round(Mean_T**2,1)      
        Mh= round((39.43 * Inertia)/T,2)
        m=round((Mh/(2*CR_Mean))*10,3)
        #print(json.dumps({"ans":[{"mean b":str(m),"s":str(CR_Mean)}]}))
        print(json.dumps({"Result":[{"Vibrational Magnetometer":"Length of the bar magnet ","Mean(length)" : str(CR_Mean),"Mean(breadth)":str(CRb_Mean),"Time period of oscillator":str(Mean_T),"Inertia":str(Inertia),"The magnetic moment of the given bar magnet(Mh)":str(Mh)+"x 10^-5 Am^2","The pole strength of the given bar magnet(m)":str(m)+"x10^-4 Am"}]}))
    def Air_wed(self):
        argument = self.arg[0:]
        def CR(x,y):
            return x+(y*0.001)
        def W5(x,y):
            return y-x
        
        CR1= round(float(argument[1],float(argument[2])),3)
        CR2= round(float(argument[5],float(argument[6])),3)
        CR3= round(float(argument[9],float(argument[10])),3)
        CR4= round(float(argument[13],float(argument[14])),3)
        CR5= round(float(argument[17],float(argument[18])),3)
        CR6= round(float(argument[21],float(argument[22])),3)
        CR7= round(float(argument[25],float(argument[26])),3)
        CR8= round(float(argument[29],float(argument[30])),3)
        CR9= round(float(argument[33],float(argument[34])),3)
        CR10= round(float(argument[37],float(argument[38])),3)
        CR11= round(float(argument[41],float(argument[42])),3)
        Width_2= round(W5(CR1,CR2),3)
        Width_3= round(W5(CR2,CR3),3)
        Width_4= round(W5(CR3,CR4),3)
        Width_5= round(W5(CR4,CR5),3)
        Width_6= round(W5(CR5,CR6),3)
        Width_7= round(W5(CR6,CR7),3)
        Width_8= round(W5(CR7,CR8),3)
        Width_9= round(W5(CR8,CR9),3)
        Width_10= round(W5(CR9,CR10),3)
        Width_11= round(W5(CR10,CR11),3)
        Mean_width2= round(Width_2/5,4)
        Mean_width3= round(Width_3/5,4)
        Mean_width4= round(Width_4/5,4)
        Mean_width5= round(Width_5/5,4)
        Mean_width6= round(Width_6/5,4)
        Mean_width7= round(Width_7/5,4)
        Mean_width8= round(Width_8/5,4)
        Mean_width9= round(Width_9/5,4)
        Mean_width10= round(Width_10/5,4)
        Mean_width11= round(Width_11/5,4)
        MeanBeta= round((Mean_width2+Mean_width3+Mean_width4+Mean_width5+Mean_width6+Mean_width7+Mean_width8+Mean_width9+Mean_width10+Mean_width11)/12,4)




