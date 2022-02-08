from cgi import print_directory
import json
import math
from typing import ValuesView

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
        argument = self.arg[0:]
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
        VB=round(trB/2,2)
        A= round((VA+VB)/4,2)
        Dtr_a=round(TR(float(argument[9]),float(argument[10])),2)
        Vtr_a=round(TR(float(argument[13]),float(argument[14])),2)
        Btr_a=round(TR(float(argument[17]),float(argument[18])),2)
        BGtr_a=round(TR(float(argument[21]),float(argument[22])),2)
        Gtr_a=round(TR(float(argument[25]),float(argument[26])),2)
        Ytr_a=round(TR(float(argument[29]),float(argument[30])),2)
        Otr_a=round(TR(float(argument[33]),float(argument[34])),2)
        Rtr_a=round(TR(float(argument[37]),float(argument[38])),2)

        Dtr_b=round(TR(float(argument[11]),float(argument[12])),2)
        Vtr_b=round(TR(float(argument[15]) ,float(argument[16])),2)
        Btr_b=round(TR(float(argument[19]),float(argument[20])),2)
        BGtr_b=round(TR(float(argument[23]),float(argument[24])),2)
        Gtr_b=round(TR(float(argument[27]),float(argument[28])),2)
        Ytr_b=round(TR(float(argument[31]),float(argument[32])),2)
        Otr_b=round(TR(float(argument[35]),float(argument[36])),2)
        Rtr_b=round(TR(float(argument[39]),float(argument[40])),2)

        vva= round((Dtr_a - Vtr_a),2)
        bva= round((Dtr_a - Btr_a),2)
        bgva=round((Dtr_a - BGtr_a),2)
        gva= round((Dtr_a - Gtr_a),2)
        yva= round((Dtr_a - Ytr_a),2)
        ova= round((Dtr_a - Otr_a),2)
        rva=round(( Dtr_a - Rtr_a),2)

        degree=360+ Dtr_b

        vvb= round((degree - Vtr_b),2)
        bvb= round((degree - Btr_b),2)
        bgvb= round((degree - BGtr_b),2)
        gvb= round((degree - Gtr_b),2)
        yvb= round((degree - Ytr_b),2)
        ovb= round((degree - Otr_b),2)
        rvb= round((degree - Rtr_b),2)

        MeanD1= round((vva+vvb)/2,2)
        MeanD2= round((bva+bvb)/2,2)
        MeanD3= round((bgva+bgvb)/2,2)
        MeanD4= round((gva+gvb)/2,2)
        MeanD5= round((yva+yvb)/2,2)
        MeanD6= round((ova+ovb)/2,2)
        MeanD7= round((rva+rvb)/2,2)

        V=round((math.sin(math.radians(A+MeanD1)/2))/(math.sin(math.radians(A/2))),4)
        B=round((math.sin(math.radians(A+MeanD2)/2))/(math.sin(math.radians(A/2))),4)        
        BG=round((math.sin(math.radians(A+MeanD3)/2))/(math.sin(math.radians(A/2))),4)        
        G=round((math.sin(math.radians(A+MeanD4)/2))/(math.sin(math.radians(A/2))),4)        
        Y=round((math.sin(math.radians(A+MeanD5)/2))/(math.sin(math.radians(A/2))),4)        
        O=round((math.sin(math.radians(A+MeanD6)/2))/(math.sin(math.radians(A/2))),4)
        R=round((math.sin(math.radians(A+MeanD7)/2))/(math.sin(math.radians(A/2))),4)       

        mu1=V
        mu2=BG
        mu3=Y
        mu4=R
        mu5=B
        mu6=G
        mu7=R
        mu8=O

        MU1 = round((mu1+mu5)/2,2)
        MU2=  round((mu2+mu6)/2,2)
        MU3=  round((mu3+mu7)/2,2)
        MU4=  round((mu8+mu4)/2,2)
        W1=round(((mu1-mu5)/(MU1-1)),4)
        W2=round(((mu2-mu6)/(MU2-1)),4)
        W3=round(((mu3-mu7)/(MU3-1)),4)
        W4=round(((mu8-mu4)/(MU4-1)),4)
        power=round((W1+W2+W3+W4)/4,4)
        print(json.dumps({"ans":[{"Angle of prism(Va)":str(VA)+"m","Angle of (VB)":str(VB)+"m","Angle of (A)":str(A)+"m","Mean_violet":str(MeanD1),"Mean_Blue":str(MeanD2),"Mean_Blush green":str(MeanD3),"Mean_green":str(MeanD4),"Mean_Yellow":str(MeanD5),"Mean_orange":str(MeanD6),"Mean_red":str(MeanD7),"μ - Violet":str(V),"μ - blue":str(B),"μ - Blush green":str(BG),"μ - green":str(G),"μ - Yellow":str(Y),"μ - Orange":str(O),"μ - red":str(R),"Mean of dispersive power of prism(D)":str(power)}]}))

    def laser(self):
        argument= self.arg[0:]
        def TR(x,y):
            return(x+(y*0.01))   
        def VA(x,y):
            return (y-x)
        cr_al= round(TR(float(argument[1]),float(argument[2])),2)
        cr_bl= round(TR(float(argument[3]),float(argument[4])),2)
        cr_ar= TR(float(argument[5]),float(argument[6]))
        cr_br= TR(float(argument[7]),float(argument[8]))
        
        DA=round(VA(cr_al,cr_ar),2)
        DB=round(VA(cr_bl,cr_br),2)
        MeanA=round((DA+DB)/4,2)
        Tan1= math.degrees(float(argument[10])/45)
        N=round((math.sin(math.radians(MeanA)))/589.3*10000,4)
        # print(json.dumps({"ans":[{"2":str(N)+"x 10^5"}]}))

        print(json.dumps({"ans":[{"2":str(Tan1)}]}))

    def newton(self):
        argument = self.arg[0:]
        def CR(x,y):
            return (x+(y*0.001))
        def D(x,y):
            return ((x-y)**2)
        def MW(x):
            return(x/5)
        def EOF1(x,y):
            return(y+(x*0.01))
        CR1=CR(float(argument[1]),float(argument[2]))
        CR2=CR(float(argument[5]),float(argument[6]))
        CR3=CR(float(argument[9]),float(argument[10]))
        CR4=CR(float(argument[13]),float(argument[14]))
        CR5=CR(float(argument[17]),float(argument[18]))
        CR6=CR(float(argument[21]),float(argument[22]))
        CR7=CR(float(argument[25]),float(argument[26]))
        CR8=CR(float(argument[29]),float(argument[30]))
        CR9=CR(float(argument[33]),float(argument[34]))
        CR10=CR(float(argument[37]),float(argument[38]))
        CR11=CR(float(argument[41]),float(argument[42]))

        CRR1=CR(float(argument[3]),float(argument[4]))
        CRR2=CR(float(argument[7]),float(argument[8]))
        CRR3=CR(float(argument[11]),float(argument[12]))
        CRR4=CR(float(argument[15]),float(argument[16]))
        CRR5=CR(float(argument[19]),float(argument[20]))
        CRR6=CR(float(argument[23]),float(argument[24]))
        CRR7=CR(float(argument[27]),float(argument[28]))
        CRR8=CR(float(argument[31]),float(argument[32]))
        CRR9=CR(float(argument[35]),float(argument[36]))
        CRR10=CR(float(argument[39]),float(argument[40]))
        CRR11=CR(float(argument[43]),float(argument[44]))

        D1= round(D(CR1,CRR1),3)
        D2= round(D(CR2,CRR2),3)
        D3= round(D(CR3,CRR4),3)
        D4= round(D(CR4,CRR4),3)
        D5= round(D(CR5,CRR5),3)
        D6= round(D(CR6,CRR6),3)
        D7= round(D(CR7,CRR7),3)
        D8= round(D(CR8,CRR8),3)
        D9= round(D(CR9,CRR9),3)
        D10= round(D(CR10,CRR10),3)
        D11= round(D(CR11,CRR11),3)

        d1= ((D6-D1))
        d2= ((D7-D2))
        d3= ((D8-D3))
        d4= ((D9-D4))
        d5= ((D10-D5))

        MeanR1=round((d1+d2+d3+d4+d5)/5,6)
        
        CR_1=CR(float(argument[45]),float(argument[46]))
        CR_2=CR(float(argument[49]),float(argument[50]))
        CR_3=CR(float(argument[53]),float(argument[54]))
        CR_4=CR(float(argument[57]),float(argument[58]))
        CR_5=CR(float(argument[61]),float(argument[62]))
        CR_6=CR(float(argument[65]),float(argument[66]))
        CR_7=CR(float(argument[69]),float(argument[70]))
        CR_8=CR(float(argument[73]),float(argument[74]))
        CR_9=CR(float(argument[77]),float(argument[78]))
        CR_10=CR(float(argument[81]),float(argument[82]))
        CR_11=CR(float(argument[85]),float(argument[86]))

        CR_R1=CR(float(argument[47]),float(argument[48]))
        CR_R2=CR(float(argument[51]),float(argument[52]))
        CR_R3=CR(float(argument[55]),float(argument[56]))
        CR_R4=CR(float(argument[59]),float(argument[60]))
        CR_R5=CR(float(argument[63]),float(argument[64]))
        CR_R6=CR(float(argument[67]),float(argument[68]))
        CR_R7=CR(float(argument[71]),float(argument[72]))
        CR_R8=CR(float(argument[75]),float(argument[76]))
        CR_R9=CR(float(argument[79]),float(argument[80]))
        CR_R10=CR(float(argument[83]),float(argument[84]))
        CR_R11=CR(float(argument[87]),float(argument[88]))

        D_1= round(D(CR_1,CR_R1),3)
        D_2= round(D(CR_2,CR_R2),3)
        D_3= round(D(CR_3,CR_R4),3)
        D_4= round(D(CR_4,CR_R4),3)
        D_5= round(D(CR_5,CR_R5),3)
        D_6= round(D(CR_6,CR_R6),3)
        D_7= round(D(CR_7,CR_R7),3)
        D_8= round(D(CR_8,CR_R8),3)
        D_9= round(D(CR_9,CR_R9),3)
        D_10= round(D(CR_10,CR_R10),3)
        D_11= round(D(CR_11,CR_R11),3)

        d_1= ((D_6-D_1))
        d_2= ((D_7-D_2))
        d_3= ((D_8-D_3))
        d_4= ((D_9-D_4))
        d_5= ((D_10-D_5))
        MeanR2=round((d_1+d_2+d_3+d_4+d_5)/5,6)
        R1= (MeanR1/353580)
        R2=(MeanR2/353580)
        R= ((R1+R2)/2)
        f1= 1/R1
        f2=1/R2
        f=f1+f2
        ftemp=1/(0.5*f)
        F=round(ftemp,10)
        print(json.dumps({"ans":[{"Mean[R1]":str(MeanR1)+"10^-4 m^2","Mean[R2]":str(MeanR2)+"10^-4 m^2","Radial of curvature of the given convex lens(R)=":str(R),"Focal length of the given convex lens(f)":str(F)}]}))


        # print(json.dumps({"ans":[{"Mean[R1]":str(CR_7)+"10^-4 m^2","Mean[R2]":str(MeanR2)+"10^-4 m^2"}]}))
