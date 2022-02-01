import json
import math
class EM1:
    def __init__(self, arg):
        self.arg = arg
    def DC_SHUNT_MOTOR(self):
        argument = self.arg[:]
        S1 = float(argument[4])-float(argument[3])
        S2 = float(argument[9])-float(argument[8])
        S3 = float(argument[14])-float(argument[13])
        S4 = float(argument[19])-float(argument[18])
        S5 = float(argument[24])-float(argument[23])
        T1 = S1*0.1035
        T2 = S2*0.1035
        T3 = S3*0.1035
        T4 = S4*0.1035
        T5 = S5*0.1035
        IP1 = float(argument[1])*1
        IP2 = float(argument[6])*2
        IP3 = float(argument[11])*3
        IP4 = float(argument[16])*4
        IP5 = float(argument[21])*5
        OP1 = (2*math.pi*float(argument[5])*T1)/60
        OP2 = (2*math.pi*float(argument[10])*T2)/60
        OP3 = (2*math.pi*float(argument[15])*T3)/60
        OP4 = (2*math.pi*float(argument[20])*T4)/60
        OP5 = (2*math.pi*float(argument[25])*T5)/60
        E1 = (OP1/IP1)*100
        E2 = (OP2/IP2)*100
        E3 = (OP3/IP3)*100
        E4 = (OP4/IP4)*100
        E5 = (OP5/IP5)*100
        E = round((E1+E2+E3+E4+E5),2)/5
        print(json.dumps({"Impact":[{"Thus load test on DC shunt motor is conducted and its efficiency is determined":str(E)+ "%" }]}))
        # print(json.dumps({"Impact":[{"Thus load test on DC shunt motor is conducted and its efficiency is determined":str(IP1)+ "%" }]}))

    def DC_SERIES_MOTOR(self):
        argument = self.arg[:]
        S1 = float(argument[4])-float(argument[3])
        S2 = float(argument[9])-float(argument[8])
        S3 = float(argument[14])-float(argument[13])
        S4 = float(argument[19])-float(argument[18])
        S5 = float(argument[24])-float(argument[23])
        T1 = S1*0.1035
        T2 = S2*0.1035
        T3 = S3*0.1035
        T4 = S4*0.1035
        T5 = S5*0.1035
        IP1 = float(argument[1])*1
        IP2 = float(argument[6])*2
        IP3 = float(argument[11])*3
        IP4 = float(argument[16])*4
        IP5 = float(argument[21])*5
        OP1 = (2*math.pi*float(argument[5])*T1)/60
        OP2 = (2*math.pi*float(argument[10])*T2)/60
        OP3 = (2*math.pi*float(argument[15])*T3)/60
        OP4 = (2*math.pi*float(argument[20])*T4)/60
        OP5 = (2*math.pi*float(argument[25])*T5)/60
        E1 = (OP1/IP1)*100
        E2 = (OP2/IP2)*100
        E3 = (OP3/IP3)*100
        E4 = (OP4/IP4)*100
        E5 = (OP5/IP5)*100
        E = (E1+E2+E3+E4+E5)/5
        print(json.dumps({"Impact":[{"Thus load test on DC series motor is conducted and its efficiency is determined":str(E)+ "%" }]}))
    def DC_COMPOUND_MOTOR(self):
        argument = self.arg[:]
        S1 = float(argument[4])-float(argument[3])
        S2 = float(argument[9])-float(argument[8])
        S3 = float(argument[14])-float(argument[13])
        S4 = float(argument[19])-float(argument[18])
        S5 = float(argument[24])-float(argument[23])
        T1 = S1*0.1035
        T2 = S2*0.1035
        T3 = S3*0.1035
        T4 = S4*0.1035
        T5 = S5*0.1035
        IP1 = float(argument[1])*1
        IP2 = float(argument[6])*2
        IP3 = float(argument[11])*3
        IP4 = float(argument[16])*4
        IP5 = float(argument[21])*5
        OP1 = (2*math.pi*float(argument[5])*T1)/60
        OP2 = (2*math.pi*float(argument[10])*T2)/60
        OP3 = (2*math.pi*float(argument[15])*T3)/60
        OP4 = (2*math.pi*float(argument[20])*T4)/60
        OP5 = (2*math.pi*float(argument[25])*T5)/60
        E1 = (OP1/IP1)*100
        E2 = (OP2/IP2)*100
        E3 = (OP3/IP3)*100
        E4 = (OP4/IP4)*100
        E5 = (OP5/IP5)*100
        E = (E1+E2+E3+E4+E5)/5
        print(json.dumps({"Impact":[{"Thus load test on DC compound motor is conducted and its efficiency is determined":str(E)+ "%" }]}))
    def SELF(self):
        print(json.dumps({"answer":[{"result":"Thus open circuit characteristics of self excited DC shunt generator are obtained and its critical resistance is determined."}]}))
    def SEPARATELY(self):
        print(json.dumps({"answer":[{"result":"Thus open circuit characteristics of separately excited DC shunt generators are obtained."}]}))
    def Load_Separately(self):
        argument = self.arg[:]
        R1 = float(argument[1])/float(argument[2])
        R2 = float(argument[3])/float(argument[4])
        R3 = float(argument[5])/float(argument[6])
        R4 = float(argument[7])/float(argument[8])
        I1 = float(argument[1])+float(argument[2])
        I2 = float(argument[4])+float(argument[5])
        I3 = float(argument[7])+float(argument[8])
        I4 = float(argument[10])+float(argument[11])
        F1 = float(argument[3])+(I1*R1)
        F2 = float(argument[6])+(I2*R2)
        F3 = float(argument[9])+(I3*R3)
        F4 = float(argument[12])+(I4*R4)
        F = (F1+F2+F3+F4)/4
        print(json.dumps({"Impact":[{"Thus load characteristics of separately excited DC shunt generator is obtained.":str(F)+ "%" }]}))
    def Load_Self(self):
        argument = self.arg[:]
        R1 = float(argument[1])/float(argument[2])
        R2 = float(argument[3])/float(argument[4])
        R3 = float(argument[5])/float(argument[6])
        R4 = float(argument[7])/float(argument[8])
        I1 = float(argument[1])+float(argument[2])
        I2 = float(argument[4])+float(argument[5])
        I3 = float(argument[7])+float(argument[8])
        I4 = float(argument[10])+float(argument[11])
        F1 = float(argument[3])+(I1*R1)
        F2 = float(argument[6])+(I2*R2)
        F3 = float(argument[9])+(I3*R3)
        F4 = float(argument[12])+(I4*R4)
        F = (F1+F2+F3+F4)/4
        print(json.dumps({"Impact":[{"Thus load characteristics of self excited DC shunt generator is obtained.":str(F)+ "%" }]}))
    def Hopkin(self):
        argument = self.arg[:]
        Ra1 = (float(argument[2])+float(argument[3]))/2
        Ra2 = (float(argument[7])+float(argument[8]))/2
        Ra3 = (float(argument[12])+float(argument[13]))/2
        R1 = (float(argument[1])/Ra1)
        R2 = (float(argument[6])/Ra2)
        R3 = (float(argument[11])/Ra3)
        M1 = ((float(argument[2])+float(argument[3]))*2)*R1
        M2 = ((float(argument[7])+float(argument[8]))*2)*R2
        M3 = ((float(argument[12])+float(argument[13]))*2)*R3
        ra1 = (float(argument[4])+float(argument[5]))/2
        ra2 = (float(argument[9])+float(argument[10]))/2
        ra3 = (float(argument[14])+float(argument[15]))/2
        r1 = (float(argument[1])/ra1)
        r2 = (float(argument[6])/ra2)
        r3 = (float(argument[11])/ra3)
        m1 = (float(argument[3])*2)*r1
        m2 = (float(argument[8])*2)*r2
        m3 = (float(argument[13])*2)*r3
        T1 = (float(argument[1])*2)-(M1+m1)
        T2 = (float(argument[6])*2)-(M2+m2)
        T3 = (float(argument[11])*2)-(M3+m3)
        #tabular2
        R11 = float(argument[16])/((float(argument[17])+float(argument[18]))/2)
        R12 = float(argument[20])/((float(argument[21])+float(argument[22]))/2)
        R13 = float(argument[24])/((float(argument[25])+float(argument[26]))/2)
        M11 = ((float(argument[17])+float(argument[18]))*2)*R11
        M12 = ((float(argument[21])+float(argument[22]))*2)*R12
        M13 = ((float(argument[25])+float(argument[26]))*2)*R13
        F1 = float(argument[16])*float(argument[19])
        F2 = float(argument[20])*float(argument[23])
        F3 = float(argument[24])*float(argument[27])
        w1 = ((float(argument[17])*2)-(M11+(float(argument[18]))))/2
        w2 = ((float(argument[21])*2)-(M12+(float(argument[22]))))/2
        w3 = ((float(argument[15])*2)-(M13+(float(argument[26]))))/2
        t1 = M11+F1+w1
        t2 = M12+F2+w2
        t3 = M13+F3+w3
        I1 = float(argument[16])*(float(argument[17])+float(argument[18]))
        I2 = float(argument[20])*(float(argument[21])+float(argument[22]))
        I3 = float(argument[24])*(float(argument[25])+float(argument[26]))
        E1 = ((I1 - t1)/I1)*100
        E2 = ((I2 - t2)/I2)*100
        E3 = ((I3 - t3)/I3)*100
        #Tabular3
        r11 = float(argument[28])/((float(argument[29])+float(argument[30]))/2)
        r12 = float(argument[31])/((float(argument[32])+float(argument[33]))/2)
        r13 = float(argument[34])/((float(argument[35])+float(argument[36]))/2)
        m11 = ((float(argument[29])+float(argument[30]))*2)*r11
        m12 = ((float(argument[32])+float(argument[33]))*2)*r12
        m13 = ((float(argument[35])+float(argument[36]))*2)*r13
        f1 = float(argument[28])*float(argument[29])
        f2 = float(argument[31])*float(argument[32])
        f3 = float(argument[34])*float(argument[35])
        i1 =(float(argument[30])*2)*r11
        i2 = (float(argument[33])*2)*r12
        i3 =(float(argument[36])*2)*r13
        W1 = (f1-m11+i1)/2
        W2 = (f2-m12+i2)/2
        W3 = (f3-m13+i3)/2
        t11 = i1+f1+W1
        t12 = i2+f2+W2
        t13 = i3+f3+W3
        o1 = float(argument[28])*float(argument[30])
        o2 = float(argument[31])*float(argument[33])
        o3 = float(argument[34])*float(argument[36])
        e1= (o1/(o1+t11))*100
        e2 = (o2/(o2+t12))*100
        e3 = (o3/(o3+t13))*100
        e=(e1+e2+e3)/3
        print(json.dumps({"answer":[{"result":"Thus the given specimen was annealed and its hardness was studied" ,"Ans" :str(e)}] }))        #Thus the given specimen was annealed and its hardness was studied.
    def Speed(self):
        print(json.dumps({"answer":[{"result":"Thus the speed control of DC Shunt Motor is obtained using Armature and Field control methods"}]}))
    def OC(self):
        print(json.dumps({"answer":[{"result":"Thus the efficiency and regulation of a transformer is predetermined by conducting open circuit test and short circuit test and the equivalent circuit is drawn."}]}))
    def OCDC(self):
        print(json.dumps({"answer":[{"result":"Thus the above experiment is simulated"}]}))
    def trf(self):
        argument = self.arg[:]
        Ra1 = float(argument[2])*float(argument[5])
        Ra2 = float(argument[9])*float(argument[12])
        Ra3 = float(argument[16])*float(argument[19])
        Ra4 = float(argument[23])*float(argument[26])
        Ra5 = float(argument[30])*float(argument[33])
        E1 = (Ra1/float(argument[7]))*100
        E2 = (Ra2/float(argument[14]))*100
        E3 = (Ra3/float(argument[21]))*100
        E4 = (Ra4/float(argument[28]))*100
        E5 = (Ra5/float(argument[35]))*100
        R1 = (1500-float(argument[1]))/float(argument[1])
        R2 = (1500-float(argument[8]))/float(argument[8])
        R3 = (1500-float(argument[15]))/float(argument[15])
        R4 = (1500-float(argument[22]))/float(argument[22])
        R5 = (1500-float(argument[29]))/float(argument[29])
        R=(R1+R2+R3+R4+R5)/5
        print(json.dumps({"answer":[{"result":"Thus the efficiency and regulation of a transformer is predetermined by conducting open circuit test and short circuit test and the equivalent circuit is drawn.","Ans":str(e)}]}))

    def SWINBURNE(self):
        argument = self.arg[:]
        Ra = 2.7
        Ia1 = float(argument[3])**2*Ra
        Ia2 = float(argument[6])**2*Ra
        Ia3 = float(argument[9])**2*Ra
        Ia4 = float(argument[12])**2*Ra
        T1 = Ia1 +(float(argument[1])*float(argument[3]))-Ia1
        T2 = Ia2 +(float(argument[4])*float(argument[6]))-Ia2
        T3 = Ia3 +(float(argument[7])*float(argument[9]))-Ia3
        T4 = Ia4 +(float(argument[10])*float(argument[12]))-Ia4
        I1 = float(argument[1])*float(argument[2])
        I2 = float(argument[4])*float(argument[5])
        I3 = float(argument[7])*float(argument[8])
        I4 = float(argument[10])*float(argument[11])
        O1 = I1-T1
        O2 = I2-T2
        O3 = I3-T3
        O4 = I4-T4
        E1 = (O1/I1)*100
        E2 = (O2/I2)*100
        E3 = (O3/I3)*100
        E4 = (O4/I4)*100
        ra = 2.7
        ia1 = float(argument[15])**2*ra
        ia2 = float(argument[18])**2*ra
        ia3 = float(argument[21])**2*ra
        ia4 = float(argument[24])**2*ra
        t1 = Ia1 +(float(argument[13])*float(argument[15]))-ia1
        t2 = Ia2 +(float(argument[16])*float(argument[18]))-ia2
        t3 = Ia3 +(float(argument[19])*float(argument[21]))-ia3
        t4 = Ia4 +(float(argument[22])*float(argument[24]))-ia4
        i1 = float(argument[13])*float(argument[14])
        i2 = float(argument[16])*float(argument[15])
        i3 = float(argument[19])*float(argument[20])
        i4 = float(argument[22])*float(argument[23])
        o1 = I1-T1
        o2 = I2-T2
        o3 = I3-T3
        o4 = I4-T4
        e1 = (o1/i1)*100
        e2 = (o2/i2)*100
        e3 = (o3/i3)*100
        e4 = (o4/i4)*100
        R1= 1.2*(float(argument[27])/float(argument[26]))
        R2= 1.2*(float(argument[30])/float(argument[29]))
        R3= 1.2*(float(argument[33])/float(argument[32]))
        R4= 1.2*(float(argument[36])/float(argument[35]))
        A1 = float(argument[25])/float(argument[26])
        A2 = float(argument[28])/float(argument[29])
        A3 = float(argument[31])/float(argument[32])
        A4 = float(argument[34])/float(argument[35])
        v1 = float(argument[27])+(A*R1)
        v2 = float(argument[30])+(A*R2)
        v3 = float(argument[33])+(A*R3)
        v4 = float(argument[36])+(A*R4)
        V=(v1+v2+v3+v4)/4
        print(json.dumps({"answer":[{"result":"Thus the efficiency and regulation of a transformer is predetermined by conducting open circuit test and short circuit test and the equivalent circuit is drawn.","Ans":str(V)}]}))

    
        



        

    












        




        





