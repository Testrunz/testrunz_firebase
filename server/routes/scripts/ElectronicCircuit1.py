import json
import math
class EC:
    def __init__(self, arg):
        self.arg = arg
    def CEA(self):
        argument = self.arg[:]
        Vin1 = 1*50
        dB1 = 20*math.log((float(argument[2])*100)/Vin1)
        dB2 = 20*math.log((float(argument[4])*100)/Vin1)
        dB3 = 20*math.log((float(argument[6])*100)/Vin1)
        dB4 = 20*math.log((float(argument[8])*100)/Vin1)
        dB5 = 20*math.log((float(argument[10])*100)/Vin1)
        dB6 = 20*math.log((float(argument[12])*100)/Vin1)
        dB7 = 20*math.log((float(argument[14])*100)/Vin1)
        dB8 = 20*math.log((float(argument[16])*100)/Vin1)
        dB9 = 20*math.log((float(argument[18])*100)/Vin1)
        dB10 = 20*math.log((float(argument[20])*100)/Vin1)
        IC=float(argument[18])
        B=float(argument[19])
        IB=IC/B
        IE=IC+IB
        VE =float(argument[20]) 
        RE=VE/IE
        VBE=float(argument[21])
        VB=VBE+VE
        VCC=float(argument[22])
        VCE=float(argument[23])
        RC=(VCC-VCE-VE)/IC
        I=IC/10
        R1=(VCC-VE)/(I+IE)
        R2 = VB/I
        print(json.dumps({"answer":[{"Result":"Thus the RC coupled amplifier circuit is designed and the frequency response is observed and the signal handling capacity and input and output impedance are measured.","Ans":R2}]}))
    def Emitter(self):
        argument = self.arg[:]
        Vin1 = 5.4
        dB1 = 20*math.log((float(argument[2])*10**2)/Vin1)
        dB2 = 20*math.log((float(argument[4])*10**2)/Vin1)
        dB3 = 20*math.log((float(argument[6])*10**2)/Vin1)
        dB4 = 20*math.log((float(argument[8])*10**2)/Vin1)
        dB5 = 20*math.log((float(argument[10])*10**2)/Vin1)
        dB6 = 20*math.log((float(argument[12])*10**2)/Vin1)
        dB7 = 20*math.log((float(argument[14])*10**2)/Vin1)
        dB8 = 20*math.log((float(argument[16])*10**2)/Vin1)
        dB9 = 20*math.log((float(argument[18])*10**2)/Vin1)
        dB10 = 20*math.log((float(argument[20])*10**2)/Vin1)
        dB11 = 20*math.log((float(argument[22])*10**2)/Vin1)
        dB12 = 20*math.log((float(argument[24])*10**2)/Vin1)
        dB=(dB1+dB2+dB3+dB4+dB5+dB6+dB7+dB8+dB9+dB10+dB11+dB12)/12
        print(json.dumps({"answer":[{"Result":"Thus the emitter coupled amplifier circuit is designed and the frequency response is observed and the signal handling capacity and input and output impedance are measured.","Ans":dB}]}))
    def Cascade(self):
        argument = self.arg[:]
        Vin1 = 2*1
        dB1 = 20*math.log((float(argument[2]))/Vin1)
        dB2 = 20*math.log((float(argument[4]))/Vin1)
        dB3 = 20*math.log((float(argument[6]))/Vin1)
        dB4 = 20*math.log((float(argument[8]))/Vin1)
        dB5 = 20*math.log((float(argument[10]))/Vin1)
        dB6 = 20*math.log((float(argument[12]))/Vin1)
        dB7 = 20*math.log((float(argument[14]))/Vin1)
        VBE=float(argument[15])
        VE = float(argument[16])
        VB=VBE+VE
        IC=float(argument[17])
        B=float(argument[18])
        IB=IC/B
        IE=IB+IC
        RE=VE/IE
        VCC=float(argument[19])
        VCE=float(argument[20])
        RC=(VCC-VCE-VE)/IC
        I=IC/10
        R1=(VCC-VE)/(I+IB)
        R2 = VB/I
        # AV=(RC//RL)/25
        print(json.dumps({"answer":[{"Result":"Thus the emitter coupled amplifier circuit is designed and the frequency response is observed and the signal handling capacity and input and output impedance are measured.","Ans":R2}]}))
    def Cascode(self):
        argument = self.arg[:]
        Vin1 = 3.4
        dB1 = 20*math.log((float(argument[2])*10**2)/Vin1)
        dB2 = 20*math.log((float(argument[4])*10**2)/Vin1)
        dB3 = 20*math.log((float(argument[6])*10**2)/Vin1)
        dB4 = 20*math.log((float(argument[8])*10**2)/Vin1)
        dB5 = 20*math.log((float(argument[10])*10**2)/Vin1)
        dB6 = 20*math.log((float(argument[12])*10**2)/Vin1)
        dB7 = 20*math.log((float(argument[14])*10**2)/Vin1)
        dB8 = 20*math.log((float(argument[16])*10**2)/Vin1)
        dB9 = 20*math.log((float(argument[18])*10**2)/Vin1)
        dB10 = 20*math.log((float(argument[20])*10**2)/Vin1)
        dB11 = 20*math.log((float(argument[22])*10**2)/Vin1)
        dB12 = 20*math.log((float(argument[24])*10**2)/Vin1)
        VE = float(argument[25])
        IC = float(argument[26])
        RE = VE/IC
        VCE1 = VCE2 = float(argument[27])
        VCC = float(argument[28])
        VRC = VCC-VCE1-VCE2-VE
        RC = VRC/IC
        R3 = 10*RE
        VBE = float(argument[29])
        VB1 = VBE+VE
        IB = VB1/R3
        VBC = VCE1+VE+(2*VBE)
        print(json.dumps({"answer":[{"Result":"Thus the cascade amplifier circuit is designed and the frequency response is observed and the signal handling capacity and input and output impedance are measured.","Ans":VBC}]}))
    def FET(self):
        argument = self.arg[:]
        Vin1 = 1
        dB1 = 20*math.log((float(argument[2]))/Vin1)
        dB2 = 20*math.log((float(argument[4]))/Vin1)
        dB3 = 20*math.log((float(argument[6]))/Vin1)
        dB4 = 20*math.log((float(argument[8]))/Vin1)
        dB5 = 20*math.log((float(argument[10]))/Vin1)
        dB6 = 20*math.log((float(argument[12]))/Vin1)
        dB7 = 20*math.log((float(argument[14]))/Vin1)
        Vin2 = 2
        DB1 = 20*math.log((float(argument[16]))/Vin2)
        DB2 = 20*math.log((float(argument[18]))/Vin2)
        DB3 = 20*math.log((float(argument[20]))/Vin2)
        DB4 = 20*math.log((float(argument[22]))/Vin2)
        DB5 = 20*math.log((float(argument[24]))/Vin2)
        DB6 = 20*math.log((float(argument[26]))/Vin2)
        DB7 = 20*math.log((float(argument[28]))/Vin2)
        DB8 = 20*math.log((float(argument[30]))/Vin2)
        DB9 = 20*math.log((float(argument[32]))/Vin2)
        DB10 = 20*math.log((float(argument[34]))/Vin2)
        IDSS = float(argument[35])
        VGS = float(argument[36])
        VP = float(argument[37])
        ID = IDSS*(1-VGS/VP)**2
        VS = float(argument[38])
        IS = float(argument[39])
        RS = VS/IS
        VG = VGS +(ID*RS)
        VDD = float(argument[40])
        R2 = VG/ID
        VR1 = VDD - VG
        R1 = VR1/ID
        VR2 =(VDD*VG)/(R1+VG)
        print(json.dumps({"answer":[{"Result":"Thus the cascode amplifier circuit is designed and the frequency response is observed and the signal handling capacity and input and output impedance are measured.","Ans":VR2}]}))
    def DARLINGTON(self):
        argument = self.arg[:]
        Vin1 = 2*0.2
        dB1 = 20*math.log((float(argument[2]))/Vin1)
        dB2 = 20*math.log((float(argument[4]))/Vin1)
        dB3 = 20*math.log((float(argument[6]))/Vin1)
        dB4 = 20*math.log((float(argument[8]))/Vin1)
        dB5 = 20*math.log((float(argument[10]))/Vin1)
        dB6 = 20*math.log((float(argument[12]))/Vin1)
        dB7 = 20*math.log((float(argument[14]))/Vin1)
        dB8 = 20*math.log((float(argument[16]))/Vin1)
        dB9 = 20*math.log((float(argument[18]))/Vin1)
        dB10 = 20*math.log((float(argument[20]))/Vin1)
        dB11 = 20*math.log((float(argument[22]))/Vin1)
        IC = float(argument[23])
        B = float(argument[24])
        IB = IC/B
        IE = IB+IC
        VE = float(argument[25])
        RE = VE/IE
        VBE = float(argument[26])
        VB = VBE +VE
        I = IC/10
        VCC = float(argument[27])
        R1 = (VCC - VB)/(I+IB)
        R2 = VB/I
        print(json.dumps({"answer":[{"Result":"Thus the darlington amplifier circuit is designed and the frequency response is observed and the signal handling capacity and input and output impedance are measured.","Ans":R2}]}))
    def RC(self):
        argument = self.arg[:]
        T1 = ((float(argument[3])*500)/(float(argument[2])))*360
        T2 = ((float(argument[8])*500)/(float(argument[7])))*360
        T3 = ((float(argument[13])*500)/(float(argument[12])))*360
        T4 = ((float(argument[18])*500)/(float(argument[17])))*360
        B = float(argument[21])
        VCC = float(argument[22])
        VBE = float(argument[23])
        IC = float(argument[24])
        VE = float(argument[25])
        VCE = VCC/2
        IB = IC/B
        IE = IB+IC
        RE =VE/IE
        VB =VBE+VE
        I = IC/10
        R1 = (VCC - VB)/(I+IB)
        RC = (VCC-VCE-VE)/IC
        R2 = VB/I
        print(json.dumps({"answer":[{"Result":"Thus the RC amplifier circuit is designed and the frequency response is observed and the signal handling capacity and input and output impedance are measured.","Ans":R2}]}))
    def LC(self):
        argument = self.arg[:]
        print(json.dumps({"answer":[{"Result":"Thus the colpitts oscillator circuit is constructed and its waveform is obtained."}]}))
    def CLAMPERS(self):
        argument = self.arg[:]
        print(json.dumps({"answer":[{"Result":"Thus the following clampers were designed and constructed and their characteristics waveforms is plotted in the graph."}]}))

    def DIFFERENTIAL(self):
        argument = self.arg[:]
        Vin1 = 1.4
        dB1 = ((float(argument[2]))/Vin1)
        dB2 = ((float(argument[4]))/Vin1)
        dB3 = ((float(argument[6]))/Vin1)
        dB4 = ((float(argument[8]))/Vin1)
        dB5 = ((float(argument[10]))/Vin1)
        dB6 = ((float(argument[12]))/Vin1)
        Vin = 2.5
        DB1 = (float(argument[14])*5)*Vin
        DB2 = (float(argument[16])*5)*Vin
        DB3 = (float(argument[18])*5)*Vin
        DB4 = (float(argument[20])*5)*Vin
        DB5 = (float(argument[22])*5)*Vin
        DB = (DB1+DB2+DB3+DB4+DB5)/5
        print(json.dumps({"answer":[{"Result":"Thus the differential amplifier is constructed and both the corresponding gain is obtained and  the CMRR is calculated.","Ans":DB}]}))
    def NEGATIVE(self):
        argument = self.arg[:]
        Vin1 = 1
        dB1 = 20*math.log((float(argument[9]))/Vin1)
        dB2 = 20*math.log((float(argument[11]))/Vin1)
        dB3 = 20*math.log((float(argument[13]))/Vin1)
        dB4 = 20*math.log((float(argument[15]))/Vin1)
        dB5 = 20*math.log((float(argument[17]))/Vin1)
        dB6 = 20*math.log((float(argument[19]))/Vin1)
        dB7 = 20*math.log((float(argument[21]))/Vin1)
        dB8 = 20*math.log((float(argument[23]))/Vin1)
        dB9 = 20*math.log((float(argument[25]))/Vin1)
        dB10 = 20*math.log((float(argument[27]))/Vin1)
        Vin = 0.6
        DB1 = 20*math.log((float(argument[29]))/Vin)
        DB2 = 20*math.log((float(argument[31]))/Vin)
        DB3 = 20*math.log((float(argument[33]))/Vin)
        DB4 = 20*math.log((float(argument[35]))/Vin)
        DB5 = 20*math.log((float(argument[37]))/Vin)
        DB6 = 20*math.log((float(argument[39]))/Vin)
        DB7 = 20*math.log((float(argument[41]))/Vin)
        DB8 = 20*math.log((float(argument[43]))/Vin)
        DB9 = 20*math.log((float(argument[45]))/Vin)
        VBE = float(argument[1])
        VCC = float(argument[2])
        VCE = VCC/math.sqrt(2)
        VE = VCC/10
        VE = float(argument[3])
        IE = float(argument[4])
        RE = VE/IE
        IC = float(argument[5])
        RC = (VCC-VE-VCE)/IC
        S = 10
        RB = (S-1)*RE
        R1 = float(argument[6])
        RB1 = float(argument[7])
        R2 = (R1*RB1)/(R1-RB1)
        print(json.dumps({"answer":[{"Result":"Thus the voltage shunt feedback amplifier circuit was constructed and the frequency response was plotted the parameter measured are given in the table."}], "bre":[{"Output" : str(R2)}]}))


    def ASTABLE(self):
        argument = self.arg[:]
        print(json.dumps({"answer":[{"Result":"Thus the astable multivibrator is  designed and its output waveforms are obtained."}]}))

    def SCHMITT(self):
        argument = self.arg[:]
        print(json.dumps({"answer":[{"Result":"Thus the schmitt trigger circuit using the transistor is designed and constructed and its performance."}]}))

    def INTEGRATOR(self):
        argument = self.arg[:]
        print(json.dumps({"answer":[{"Result":"Thus the RC differentiator and RC integrator was designed and constructed."}]}))


    





    





