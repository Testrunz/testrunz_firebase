import json
import math
class EE:
    def __init__(self, arg):
        self.arg = arg
    def single_trf(self):
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
        E=(E1+E2+E3+E4+E5)/5
        R=(R1+R2+R3+R4+R5)/5
        print(json.dumps({"answer":[{"result":"Thus the efficiency and regulation of a transformer is predetermined by conducting open circuit test and short circuit test and the equivalent circuit is drawn.","Efficiency":str(E),"Regulation":str(R)}]}))
    def INDUCTION(self):
        argument = self.arg[0:]
        #Torque
        T1 = 9.81*((float(argument[3])-float(argument[4]))+2)*0.0986
        T2 = 9.81*((float(argument[10])-float(argument[11]))+2)*0.0986
        T3 = 9.81*((float(argument[17])-float(argument[18]))+2)*0.0986
        T4 = 9.81*((float(argument[24])-float(argument[25]))+2)*0.0986
        T5 = 9.81*((float(argument[31])-float(argument[32]))+2)*0.0986
                      
        #input
        IP1 = float(argument[5]) * float(argument[6])
        IP2 = float(argument[12]) * float(argument[13])
        IP3 = float(argument[19]) * float(argument[20])
        IP4 = float(argument[26]) * float(argument[27])
        IP5 = float(argument[33]) * float(argument[34])

            #output
        OP1 = (2*math.pi*float(argument[7])*T1)/60
        OP2 = (2*math.pi*float(argument[14])*T2)/60
        OP3 = (2*math.pi*float(argument[21])*T3)/60
        OP4 = (2*math.pi*float(argument[28])*T4)/60
        OP5 = (2*math.pi*float(argument[35])*T5)/60

        #Eff
        Eff1 = (OP1/IP1)*100
        Eff2 = (OP2/IP2)*100
        Eff3 = (OP3/IP3)*100
        Eff4 = (OP4/IP4)*100
        Eff5 = (OP5/IP5)*100
        Eff = (Eff1 + Eff2 + Eff3 + Eff4 + Eff5)/5

        Ns = 1500
        Reg1 = ((Ns - float(argument[7]))/Ns)*100
        Reg2 = ((Ns - float(argument[14]))/Ns)*100
        Reg3 = ((Ns - float(argument[21]))/Ns)*100
        Reg4 = ((Ns - float(argument[29]))/Ns)*100
        Reg5 = ((Ns - float(argument[36]))/Ns)*100
        Reg = (Reg1 + Reg2 + Reg3 + Reg4 + Reg5)/5
        print(json.dumps({"Mean":[{"The efficiency of single phase induction motor is" : str(Eff)}] , "Mean":[{"The Regularity is" : str(Reg)}]}))
        