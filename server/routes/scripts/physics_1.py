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
            return (x+(y*0.001))
        def W5(x,y):
            return (y-x)
        def MW(x):
            return(x/5)
        def EOF1(x,y):
            return(y+(x*0.01))
        CR1= CR(float(argument[1]),float(argument[2]))
        CR2= CR(float(argument[3]),float(argument[4]))
        CR3= CR(float(argument[5]),float(argument[6]))
        CR4= CR(float(argument[7]),float(argument[8]))
        CR5= CR(float(argument[9]),float(argument[10]))
        CR6= CR(float(argument[11]),float(argument[12]))
        CR7= CR(float(argument[13]),float(argument[14]))
        CR8= CR(float(argument[15]),float(argument[16]))
        CR9= CR(float(argument[17]),float(argument[18]))
        CR10=CR(float(argument[19]),float(argument[20]))
        CR11=CR(float(argument[21]),float(argument[22]))
        Width_2= (W5(CR1,CR2))
        Width_3= (W5(CR2,CR3))
        Width_4= (W5(CR3,CR4))
        Width_5= (W5(CR4,CR5))
        Width_6= (W5(CR5,CR6))
        Width_7= (W5(CR6,CR7))
        Width_8= (W5(CR7,CR8))
        Width_9= (W5(CR8,CR9))
        Width_10= (W5(CR9,CR10))
        Width_11= (W5(CR10,CR11))
        Mean_width2= MW(Width_2)
        Mean_width3= MW(Width_3)
        Mean_width4= MW(Width_4)
        Mean_width5= MW(Width_5)
        Mean_width6= MW(Width_6)
        Mean_width7= MW(Width_7)
        Mean_width8= MW(Width_8)
        Mean_width9= MW(Width_9)
        Mean_width10=MW (Width_10)
        Mean_width11= MW(Width_11)
        MeanBeta= round((Mean_width2 + Mean_width3+Mean_width4+Mean_width5+Mean_width6+Mean_width7+Mean_width8+Mean_width9+Mean_width10+Mean_width11)/12,4)
        R1 = EOF1(float(argument[24]),float(argument[23]))
        R2 = CR(float(argument[25]),float(argument[26]))
        l= round(R2-R1,3)
        t= round(((5896*l)/(2*MeanBeta)),3)
        ts=t/100000
        print(json.dumps({"ans":[{"Mean frindge width(β)":str(MeanBeta),"The distance between edge of contact and wire(l)":str(l)+"m","Thickness of given specimen is found by forming interfernce fringe using air wedge arrangement - Thickness ofspeciemnt(t)=":str(ts)}]}))
    def prism(self): 
        argument = self.arg[1:]
        def TR(x,y):
            return(x+(y*0.01))   
        def VA(x,y):
            return (y-x)
        def VB(x,y):
            return(x-y)
        tr_al= TR(float(argument[1]),float(argument[2]))
        tr_bl= TR(float(argument[3]),float(argument[4]))
        tr_ar= TR(float(argument[5]),float(argument[6]))
        tr_br= TR(float(argument[7]),float(argument[8]))
        trA= VA(tr_al,tr_ar)
        trB=VB(tr_bl,tr_br)
        VA= round(trA,2)
        VB=round(trB/2)
        A= round((VA+VB)/4,2)
        print(json.dumps({"ans":[{"Angle of prism(Va)":str(VA)+"m","Angle of (VB)":str(VB)+"m","Angle of (A)":str(A)+"m"}]}))
        Dtr_a=TR(float(argument[9]),float(argument[10]))
        Vtr_a=TR(float(argument[13]),float(argument[14]))
        Btr_a=TR(float(argument[17]),float(argument[18]))
        BGtr_a=TR(float(argument[21]),float(argument[22]))
        Gtr_a=TR(float(argument[25]),float(argument[26]))
        Ytr_a=TR(float(argument[29]),float(argument[30]))
        Otr_a=TR(float(argument[33]),float(argument[34]))
        Rtr_a=TR(float(argument[37]),float(argument[38]))

        Dtr_b=TR(float(argument[11]),float(argument[12]))
        Vtr_b=TR(float(argument[15]) ,float(argument[16]))
        Btr_b=TR(float(argument[19]),float(argument[20]))
        BGtr_b=TR(float(argument[23]),float(argument[24]))
        Gtr_b=TR(float(argument[27]),float(argument[28]))
        Ytr_b=TR(float(argument[31]),float(argument[32]))
        Otr_b=TR(float(argument[35]),float(argument[36]))
        Rtr_b=TR(float(argument[39]),float(argument[40]))

        vva= Dtr_a - Vtr_a
        bva= Dtr_a - Btr_a
        bgva= Dtr_a - BGtr_a
        gva= Dtr_a - Gtr_a
        yva= Dtr_a - Ytr_a
        ova= Dtr_a - Otr_a
        rva= Dtr_a - Rtr_a

        vvb= Dtr_b - Vtr_b
        bvb= Dtr_b - Btr_b
        bgvb= Dtr_b - BGtr_b
        gvb= Dtr_b - Gtr_b
        yvb= Dtr_b - Ytr_b
        ovb= Dtr_b - Otr_b
        rvb= Dtr_b - Rtr_b
        VA= trA/2
        VB=trB/2
        A= (VA+VB)/4
        print(json.dumps({"ans":[{"Angle of prism(VB)":str(VA)+"m","Angle of (A)":str(VB)+"m"}]}))
        print(json.dumps({"ans":[{"d":str(vvb),"s":str(bvb),"e":str(bgvb),"r":str(gvb),"y":str(yvb),"o":str(ovb),"u":str(rvb)}]}))



