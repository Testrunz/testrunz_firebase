import json
import math as m

class FML:
    def __init__(self, arg):
        self.arg = arg

    def Through_Pipe(self):
        argument = self.arg[0:]
        #print(argument)got output
        d = float(argument[1])
        A = float(argument[2])
        h = float(argument[3])
        l = float(argument[4])
        a= (m.pi/4)*d**2
        H1 = float(argument[5])- float(argument[6])
        H2 = float(argument[8])- float(argument[9])
        H3 = float(argument[11])- float(argument[12])
        Qact1 =(A*h)/(float(argument[7]))
        Qact2 =(A*h)/(float(argument[10]))
        Qact3 =(A*h)/(float(argument[13]))
        V1 = (Qact1/a)
        V2 = (Qact2/a)
        V3 = (Qact3/a)
        K1 = ((2*9.81*d*H1*10**-2)/(4*l*V1**2))
        K2 = ((2*9.81*d*H2*10**-2)/(4*l*V2**2))
        K3 = ((2*9.81*d*H3*10**-2)/(4*l*V3**2))
        K= (K1+K2+K3)/3
        print(json.dumps({"pipe":[{"The coefficient of friction of diameter of pipe is" : str(K)}]}))

    def Venturimeter(self):
        argument = self.arg[0:]
        #print(argument)got output
        Sm =float(argument[5])
        S =float(argument[6])
        A = float(argument[7])
        h =float(argument[3])
        a1= (m.pi/4)*float(argument[1])**2
        a2= (m.pi/4)*float(argument[2])**2
        H1 = float(argument[8])- float(argument[9])*((Sm-S)/S)
        H2 = float(argument[11])- float(argument[12])*((Sm-S)/S)
        H3 = float(argument[14])- float(argument[15])*((Sm-S)/S)
        H4 = float(argument[17])- float(argument[18])*((Sm-S)/S)
        Qact1 =(A*h)/(float(argument[10]))
        Qact2 =(A*h)/(float(argument[13]))
        Qact3 =(A*h)/(float(argument[16]))
        Qact4 =(A*h)/(float(argument[19]))
        Qth1 = ((a1*a2)*m.sqrt(2*9.81*H1*10**-2))/m.sqrt(a1**2-a2**2)
        Qth2 = ((a1*a2)*m.sqrt(2*9.81*H2*10**-2))/m.sqrt(a1**2-a2**2)
        Qth3 = ((a1*a2)*m.sqrt(2*9.81*H3*10**-2))/m.sqrt(a1**2-a2**2)
        Qth4 = ((a1*a2)*m.sqrt(2*9.81*H4*10**-2))/m.sqrt(a1**2-a2**2)
        Q1 = ((Qact1/Qth1)+(Qact2/Qth2)+(Qact3/Qth3)+(Qact4/Qth4))/4
        print(json.dumps({"Ven":[{"The coefficient of the discharge of given Venturi metre" : str(Q1) }]}))
    
    def Jet(self):
        argument = self.arg[0:]
        #print(argument)got output
        A = float(argument[3])
        h = float(argument[6])
        a= (m.pi/4)*float(argument[1])**2
        Qact1 =(A*h)/(float(argument[8]))
        Qact2 =(A*h)/(float(argument[10]))
        Qact3 =(A*h)/(float(argument[12]))
        Qact4 =(A*h)/(float(argument[14]))
        Qact5 =(A*h)/(float(argument[16]))
        V1 = Qact1/a
        V2 = Qact1/a
        V3 = Qact1/a
        V4 = Qact1/a
        V5 = Qact1/a
        F1 = 1000*a*V1**2
        F2 = 1000*a*V2**2
        F3 = 1000*a*V3**2
        F4 = 1000*a*V4**2
        F5 = 1000*a*V5**2   
        E1 = (((float(argument[9])*10**4*float(argument[4])) /(F1*float(argument[5])))*100)            
        E2 = (((float(argument[11])*10**4*float(argument[4])) /(F2*float(argument[5])))*100)
        E3 = (((float(argument[13])*10**4*float(argument[4])) /(F3*float(argument[5])))*100)
        E4 = (((float(argument[15])*10**4*float(argument[4])) /(F4*float(argument[5])))*100)
        E5 = (((float(argument[17])*10**4*float(argument[4])) /(F5*float(argument[5])))*100)
        E = (E1+E2+E3+E4+E5)/5
        print(json.dumps({"Jet":[{"The efficiency of the jet is determined by the method of impact of Jet on curved vanes is " : str(E) }]}))

    def Centrifugal(self):
        argument = self.arg[0:]
        #Got output
        A = float(argument[1])
        h = float(argument[2])
        H1 = float(argument[7])+float(argument[9])+float(argument[3])
        H2 = float(argument[13])+float(argument[15])+float(argument[3])
        H3 = float(argument[19])+float(argument[21])+float(argument[3])
        Qact1 =(A*h)/(float(argument[10]))
        Qact2 =(A*h)/(float(argument[16]))
        Qact3 =(A*h)/(float(argument[22]))
        I1 = (3600*float(argument[5]))/(float(argument[4])*float(argument[11]))
        I2 = (3600*float(argument[5]))/(float(argument[4])*float(argument[17]))
        I3 = (3600*float(argument[5]))/(float(argument[4])*float(argument[23]))
        Q1 =  ((9810*Qact1*H1)/1000)
        Q2	=((9810*Qact2*H2)/1000)
        Q3 = ((9810*Qact3*H3)/1000)
        E = (((Q1/I1)*100)+((Q2/I2)*100)+((Q3/I3)*100))/4
        print(json.dumps({"Centrifugal":[{"the performance characteristics of centrifugal pump was studied and the maximum efficiency is calculated from the graph as " : str(E) }]}))

    def Submersible(self):
        argument = self.arg[0:]
        #print(argument)got output
        A = float(argument[1])
        h =float(argument[4])
        H1 = float(argument[6])+float(argument[7])+float(argument[3])
        H2 = float(argument[10])+float(argument[11])+float(argument[3])
        H3 = float(argument[14])+float(argument[15])+float(argument[3])
        H4 = float(argument[18])+float(argument[19])+float(argument[3])
        Qact1 =(A*h)/(float(argument[9]))
        Qact2 =(A*h)/(float(argument[13]))
        Qact3 =(A*h)/(float(argument[17]))
        Qact4 =(A*h)/(float(argument[21]))
        I1 = (3600*float(argument[5]))/(float(argument[2])*float(argument[8]))
        I2 = (3600*float(argument[5]))/(float(argument[2])*float(argument[12]))
        I3 = (3600*float(argument[5]))/(float(argument[2])*float(argument[16]))
        I4 = (3600*float(argument[5]))/(float(argument[2])*float(argument[20]))
        Q1 = (9810*Qact1*H1)/1000
        Q2	=(9810*Qact2*H2)/1000
        Q3 = (9810*Qact3*H3)/1000
        Q4 =(9810*Qact4*H4)/1000
        E = (((Q1/I1)*100)+((Q2/I2)*100)+((Q3/I3)*100)+((Q4/I4)*100))/4
        print(json.dumps({"Submersible":[{"The efficiency of the Submersible is " : str(E) }]}))

    def Reciprocating(self):
        argument = self.arg[0:]
        #print(argument)
        A = float(argument[1])
        h =float(argument[6])
        d =float(argument[2])
        l =float(argument[7])
        H1 = float(argument[9])+float(argument[11])+float(argument[4])
        H2 = float(argument[16])+float(argument[18])+float(argument[4])
        H3 = float(argument[23])+float(argument[25])+float(argument[4])
        Qact1 =(A*h)/(float(argument[12]))
        Qact2 =(A*h)/(float(argument[19]))
        Qact3 =(A*h)/(float(argument[26]))
        I1 = (3600*float(argument[5]))/(float(argument[3])*float(argument[13]))
        I2 = (3600*float(argument[5]))/(float(argument[3])*float(argument[20]))
        I3 = (3600*float(argument[5]))/(float(argument[3])*float(argument[27]))
        Q1 =  ((9810*Qact1*H1)/1000)
        Q2	=((9810*Qact2*H2)/1000)
        Q3 = ((9810*Qact3*H3)/1000)
        E = (((Q1/I1)*100)+((Q2/I2)*100)+((Q3/I3)*100))/3
        Qth1 = (m.pi*d**2*l*float(argument[14]))/(4*60)
        Qth2 = (m.pi*d**2*l*float(argument[21]))/(4*60)
        Qth3 = (m.pi*d**2*l*float(argument[28]))/(4*60)
        S1 = ((Qth1-Q1)/Qth1)*100
        S2 = ((Qth2-Q2)/Qth2)*100
        S3 = ((Qth3-Q3)/Qth3)*100
        S = (S1+S2+S3)/4
        print(json.dumps({"Submersible":[{"The efficiency of the Reciprocating is " : str(S)}]}))


    def Orifice(self):
        argument = self.arg[0:]
        CA =float(argument[1])
        CG =float(argument[2])
        FA = float(argument[3])
        FG =float(argument[4])
        print(json.dumps({"length":[{"Constant Head Analytical Method" : str(CA)}], "breadth":[{"Constant Head Graphical Method" : str(CG)}], "average_time":[{"Falling Head Analytical Method " : str(FA)}], "interia":[{"Falling Head Graphical Method " : str(FG) }] }))

    
    def Minor_Loss(self):
        argument = self.arg[0:]
        #print(argument)got outpu
        d1 = float(argument[1])
        d2 = float(argument[2])
        h = float(argument[3])
        A = float(argument[4])
        a1= (m.pi/4)*d1**2
        a2= (m.pi/4)*d2**2
        H1 = float(argument[17])- float(argument[18])
        H2 = float(argument[20])- float(argument[21])
        H3 = float(argument[23])- float(argument[24])
        Qact1 =(A*h)/(2*float(argument[19]))
        Qact2 =(A*h)/(2*float(argument[22]))
        Qact3 =(A*h)/(2*float(argument[25]))
        V11 = (Qact1/a1)
        V12 = (Qact2/a1)
        V13 = (Qact3/a1)
        V21 = (Qact1/a2)
        V22 = (Qact2/a2)
        V23 = (Qact3/a2)
        K = (((2*9.81*H1*10**-2)/(V11-V21)**2)+((2*9.81*H2*10**-2)/(V12-V22)**2)+((2*9.81*H3*10**-2)/(V13-V23)**2))/3
        #print(json.dumps({"MO":[{"Loss of head due to expansion " : str(K) }]}))
        
        td1 = float(argument[5])
        td2 = float(argument[6])
        th = float(argument[7])
        tA = float(argument[8])
        ta1= (m.pi/4)*td1**2
        ta2= (m.pi/4)*td2**2
        tH1 = float(argument[26])- float(argument[27])
        tH2 = float(argument[29])- float(argument[30])
        tH3 = float(argument[32])- float(argument[33])
        tH4 = float(argument[35])- float(argument[36])
        tQact1 =(tA*th)/(2*float(argument[28]))
        tQact2 =(tA*th)/(2*float(argument[31]))
        tQact3 =(tA*th)/(2*float(argument[34]))
        tQact4 =(tA*th)/(2*float(argument[37]))
        tV11 = (tQact1/ta1)
        tV12 = (tQact2/ta1)
        tV13 = (tQact3/ta1)
        tV14 = (tQact4/ta1)
        tV21 = (tQact1/ta2)
        tV22 = (tQact2/ta2)
        tV23 = (tQact3/ta2)
        tV24 = (tQact4/ta2)
        tK = (((2*9.81*tH1*10**-2)/(tV11-tV21)**2)+((2*9.81*tH2*10**-2)/(tV12-tV22)**2)+((2*9.81*tH3*10**-2)/(tV13-tV23)**2)+((2*9.81*tH4*10**-2)/(tV14-tV24)**2))/4
        #print(json.dumps({"ML":[{"Loss of head due to Contraction " : str(tK) }]}))
#3
        Td1 = float(argument[9])
        TA = float(argument[12])
        Th = float(argument[11])
        Ta1= (m.pi/4)*Td1**2
        TH1 = float(argument[38])- float(argument[39])
        TH2 = float(argument[41])- float(argument[42])
        TH3 = float(argument[44])- float(argument[45])
        TH4 = float(argument[47])- float(argument[48])
        TQact1 =(TA*Th)/(2*float(argument[40]))
        TQact2 =(TA*Th)/(2*float(argument[43]))
        TQact3 =(TA*Th)/(2*float(argument[46]))
        TQact4 =(TA*Th)/(2*float(argument[49]))
        TV11 = (TQact1/Ta1)
        TV12 = (TQact2/Ta1)
        TV13 = (TQact3/Ta1)
        TV14 = (TQact4/Ta1)
        TK = (((2*9.81*TH1*10**-2)/(TV11)**2)+((2*9.81*TH2*10**-2)/(TV12)**2)+((2*9.81*TH3*10**-2)/(TV13)**2)+((2*9.81*TH4*10**-2)/(TV14)**2))/4
        #print(json.dumps({"MH":[{"Loss of head due to elbow " : str(TK) }]}))
#4
        T1d1 = float(argument[13])
        T1A = float(argument[16])
        T1h = float(argument[15])
        T1a1= (m.pi/4)*T1d1**2
        T1H1 = float(argument[50])- float(argument[51])
        T1H2 = float(argument[53])- float(argument[51])
        T1H3 = float(argument[56])- float(argument[57])
        T1Qact1 =(T1A*T1h)/(2*float(argument[52]))
        T1Qact2 =(T1A*T1h)/(2*float(argument[55]))
        T1Qact3 =(T1A*T1h)/(2*float(argument[58]))
        T1V11 = (T1Qact1/T1a1)
        T1V12 = (T1Qact2/T1a1)
        T1V13 = (T1Qact3/T1a1)
        T1K = (((2*9.81*T1H1*10**-2)/(T1V11)**2)+((2*9.81*T1H2*10**-2)/(T1V12)**2)+((2*9.81*T1H3*10**-2)/(T1V13)**2))/3
        #print(json.dumps({"MD":[{"Loss due to bend " : str(T1K) }]}))
        print(json.dumps({"length":[{"Loss of head due to expansion " : str(K),"Loss of head due to Contraction " : str(tK)}], "breadth":[{"Loss of head due to elbow " : str(TK), "Loss due to bend " : str(T1K) }] }))