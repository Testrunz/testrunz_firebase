import json
import math
class EM2:
    def __init__(self, arg):
        self.arg = arg
        
    def NO_LOAD_AND_BLOCKED(self):
        argument = self.arg[0:]
        W11 = (float(argument[3])+float(argument[4]))*2
        W12 = (float(argument[8])+float(argument[9]))*2
        W13 = (float(argument[13])+float(argument[14]))*2
        W1 = (W11+W12+W13)/3
        W21 = (float(argument[18])+float(argument[19]))*2
        W22 = (float(argument[23])+float(argument[24]))*2
        W23 = (float(argument[28])+float(argument[29]))*2
        W2 = (W21+W22+W23)/3
        print(json.dumps({"Test":[{"The  No load test induction motor" : str(W1)}], "Test":[{"The Blocked rotor test induction motor" : str(W2)}]}))
        
    def SLIP_RING_INDUCTION_MOTOR (self):
        argument = self.arg[0:]
        T1 = 9.81*((float(argument[5])-float(argument[6]))+2)*0.0986
        T2 = 9.81*((float(argument[12])-float(argument[13]))+2)*0.0986
        T3 = 9.81*((float(argument[19])-float(argument[20]))+2)*0.0986
                      
        #input
        IP1 = float(argument[3]) * float(argument[4])
        IP2 = float(argument[10]) * float(argument[11])
        IP3 = float(argument[17]) * float(argument[18])
            #output
        OP1 = (2*math.pi*float(argument[7])*T1)/60
        OP2 = (2*math.pi*float(argument[14])*T2)/60
        OP3 = (2*math.pi*float(argument[21])*T3)/60

        #Eff
        Eff1 = (OP1/IP1)*100
        Eff2 = (OP2/IP2)*100
        Eff3 = (OP3/IP3)*100
        Eff = (Eff1 + Eff2 + Eff3)/3
        print(json.dumps({"Mean":[{"The Slip Ring induction motor observed as" : str(Eff)}]}))

        
    def V_AND_INVERTED_V(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The  ‘V’ AND ‘INVERTED V’ CURVES OF SYNCHRONOUS  MOTOR is completed sucessfully"}]}))
        
        
    def SINGLE_PHASE_INDUCTION(self):
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
        Reg4 = ((Ns - float(argument[28]))/Ns)*100
        Reg5 = ((Ns - float(argument[35]))/Ns)*100
        Reg = (Reg1 + Reg2 + Reg3 + Reg4 + Reg5)/5
        print(json.dumps({"Mean":[{"The efficiency of single phase induction motor is" : str(Eff)}] , "Mean":[{"The Regularity is" : str(Reg)}]}))
        
        
    def Direct_and_Quadrature_axis(self):
        argument = self.arg[0:]
        xd1 = float(argument[2])/float(argument[5])
        xd2 = float(argument[7])/float(argument[10])
        xd3 = float(argument[12])/float(argument[15])
        xd =(xd1+xd2+xd3)/3
        xq1 = float(argument[3])/float(argument[4])
        xq2= float(argument[8])/float(argument[8])
        xq3= float(argument[14])/float(argument[13])
        xq=(xq1+xq2+xq3)/3
        print(json.dumps({"Mean":[{"The the direct axis reactance Xd is" : str(xd)}] , "Mean":[{"The quadrature axis reactance Xq is" : str(xq)}]}))
          
    def Three_phase(self):
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
        Reg4 = ((Ns - float(argument[28]))/Ns)*100
        Reg5 = ((Ns - float(argument[35]))/Ns)*100
        Reg = (Reg1 + Reg2 + Reg3 + Reg4 + Reg5)/5
        print(json.dumps({"Mean":[{"The efficiency of three induction motor is" : str(Eff)}] , "Mean":[{"The Regularity is" : str(Reg)}]}))
 
    def LCT(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The LCT is completed sucessfully"}]}))
        
        
    def DM(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The DM completed sucessfully"}]}))
        
        
    def FREQUENCY_SYNTHESIZER(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The FREQUENCY SYNTHESIZER is completed sucessfully"}]}))

    def ASK(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The ASK is completed sucessfully"}]}))
        
        
    def BPSK(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The BPSK completed sucessfully"}]}))
        
        
    def FSK(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"The FSK is completed sucessfully"}]}))