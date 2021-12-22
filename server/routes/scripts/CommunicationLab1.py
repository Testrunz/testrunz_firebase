import json
import math
class CL1:
    def __init__(self, arg):
        self.arg = arg
    def Tuned(self):
        argument = self.arg[:]
        Vin=3*0.8
        G1 = float(argument[6])/Vin
        G2 = float(argument[8])/Vin
        G3 = float(argument[10])/Vin
        G4 = float(argument[12])/Vin
        DB1 = 20*math.log(G1)
        DB2 = 20*math.log(G2)
        DB3 = 20*math.log(G3)
        DB4 = 20*math.log(G4)
        vin=3*0.8
        g1 = float(argument[14])/vin
        g2 = float(argument[16])/vin
        g3 = float(argument[18])/vin
        g4 = float(argument[20])/vin
        dB1 = 20*math.log(g1)
        dB2 = 20*math.log(g2)
        dB3 = 20*math.log(g3)
        dB4 = 20*math.log(g4)
        T1 = float(argument[1])-float(argument[2])
        T2 = float(argument[3])-float(argument[4])
        print(json.dumps({"length":[{"Result":"Thus the tuned amplifier and wide amplifier are constructed and their frequency response also determined."}], "breadth":[{"BW for tuned" : str(T1)+"Hz"}], "width":[{"B.W for wideband" : str(T2)+"HZ"}]}))
    def Frequency(self):
        argument = self.arg[:]
        G1 = float(argument[1])*5
        G2 = float(argument[5])*5
        G3 = float(argument[9])*5
        print(json.dumps({"answer":[{"Result":"The frequency modulator and demodulator circuits are constructed and the output waveform is observed"}]}))        #Thus the given specimen was annealed and its hardness was studied.

    def Amplitude(self):
        argument = self.arg[:]
        G1=float(argument[1])*float(argument[2])
        G2=float(argument[6])*float(argument[7])
        G3=float(argument[11])*float(argument[12])
        G4=float(argument[16])*float(argument[17])
        G5=float(argument[18])*float(argument[19])
        T1=float(argument[3])*float(argument[4])
        T2=float(argument[8])*float(argument[9])
        T3=float(argument[13])*float(argument[14])
        T4=float(argument[20])*float(argument[21])
        M=(G3-G4)/(G3+G4)
        print(json.dumps({"Centrifugal":[{"The amplitude modulator and demodulator circuits was constructed and their output waveform with observed, Modulation Index =":str(M)}]}))

    def emphasis(self):
        argument = self.arg[:]
        G1 = float(argument[2])*0.2
        G2 = float(argument[5])*0.2
        G3 = float(argument[8])*0.2
        G4 = float(argument[11])*0.2
        G5 = float(argument[14])*0.2
        g1 = float(argument[3])*0.2
        g2 = float(argument[6])*0.2
        g3 = float(argument[9])*0.2
        g4 = float(argument[12])*0.2
        g5 = float(argument[15])*0.2
        Gain1= 20*math.log(G1)
        Gain2= 20*math.log(G2)
        Gain3= 20*math.log(G3)
        Gain4= 20*math.log(G4)
        Gain5= 20*math.log(G5)
        gain1= 20*math.log(g1)
        gain2= 20*math.log(g2)
        gain3= 20*math.log(g3)
        gain4= 20*math.log(g4)
        gain5= 20*math.log(g5)
        print(json.dumps({"answer":[{"Result":"The pre Emphasis and De Emphasis are constructed and frequency response is determined."}]}))
    def Sample(self):
        argument = self.arg[:]
        G1=float(argument[1])*float(argument[2])
        G2=float(argument[6])*float(argument[7])
        G3=float(argument[11])*float(argument[12])
        T1=float(argument[3])*float(argument[4])
        T2=float(argument[8])*float(argument[9])
        T3=float(argument[13])*float(argument[14])
        g1=float(argument[16])*float(argument[17])
        g2=float(argument[21])*float(argument[22])
        g3=float(argument[26])*float(argument[27])
        g4=float(argument[31])*float(argument[32])
        t1=float(argument[18])*float(argument[19])
        t2=float(argument[23])*float(argument[24])
        t3=float(argument[28])*float(argument[29])
        t4=float(argument[33])*float(argument[34])
        print(json.dumps({"answer":[{"Result":" Thus the sample and hold circuit and PAM circuit are constructed under operation both studied."}]}))
    def Automatic(self):
        argument = self.arg[:]
        G1=float(argument[2])*float(argument[3])
        G2=float(argument[8])*float(argument[9])
        G3=float(argument[14])*float(argument[15])
        G4=float(argument[20])*float(argument[21])
        G5=float(argument[26])*float(argument[27])
        G6=float(argument[32])*float(argument[33])
        g1=float(argument[5])*float(argument[6])
        g2=float(argument[11])*float(argument[12])
        g3=float(argument[17])*float(argument[18])
        g4=float(argument[23])*float(argument[24])
        g5=float(argument[29])*float(argument[30])
        g6=float(argument[35])*float(argument[36])
        print(json.dumps({"answer":[{"Result":"Thus the sample AGC circle is constructed and it performance characteristics was studied"}]}))
    def Delayed(self):
        argument = self.arg[:]
        G1 = float(argument[2])*20
        G2 = float(argument[4])*20
        G3 = float(argument[6])*20
        print(json.dumps({"answer":[{"Result":"The delayed automatic gain control circuit is constructed and its performance is studied."}]}))
    def Pulse(self):
        argument = self.arg[:]
        G1=float(argument[1])*float(argument[2])
        G2=float(argument[6])*float(argument[7])
        G3=float(argument[11])*float(argument[12])
        G4=float(argument[16])*float(argument[17])
        T1=float(argument[3])*float(argument[4])
        T2=float(argument[8])*float(argument[9])
        T3=float(argument[13])*float(argument[14])
        T4=float(argument[18])*float(argument[19])
        print(json.dumps({"answer":[{"Result":" Thus the pulse width modulator and Pulse position modulation waveform are constructed and their operation are studied."}]}))
    def Mixer(self):
        argument = self.arg[:]
        G1 = float(argument[1])*2
        G2 = float(argument[4])*2
        G3 = float(argument[7])*2
        g1 = float(argument[2])*2
        g2 = float(argument[5])*2
        g3 = float(argument[8])*2
        R=(float(argument[22])-float(argument[18]))/(float(argument[22])+float(argument[18]))
        print(json.dumps({"answer":[{"Result":"Thus the frequency mixer and ring  modulator circuits are constructed and their performance characteristics are studied."}], "breadth":[{"Modulation Index":str(R)}]}))





