import json
import math


class PowerEle:
    def __init__(self, arg):
        self.arg = arg
    def Gate_Pulse_Generation(self):
        argument = self.arg[0:]
        #print(argument)
        print(json.dumps({"Software":"Thus the R, RC &UJT triggering circuit for SCR was constructed and its output waveforms were plotted"}))
                  
    def CHARACTERISTICS_OF_SCR(self):
        argument = self.arg[1:]
        print(json.dumps({"Software":"Thus the Characteristics of SCR and the Output waveforms were obtained."}))

    def CHARACTERISTICS_OF_TRIAC(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Thus the Characteristics of TRIAC and the Output waveforms were obtained."}]}))
                      
    def MOSFET_IGBT(self):
        argument = self.arg[0:]
        print(json.dumps({"Mean":[{"Thus the Characteristics of MOSFET & IGBT were obtained."}]}))

                      
    def HALF_CONTROLLED(self):
        argument = self.arg[0:]
        print(json.dumps({"Mean":[{"Thus a single-phase half controlled converter was constructed and their Output waveforms were plotted."}]}))
        
                     
    def FULLY_CONTROLLED(self):
        argument = self.arg[0:]
        print(json.dumps({"Mean":[{"Thus a single-phase half controlled converter was constructed and their Output waveforms were plotted."}]}))

    def MOSFET_BASED_CHOPPERS(self):
        argument = self.arg[0:]
        #Stepup
        Vs=2.8
        K1 = float(argument[1])/float(argument[3])
        K2 = float(argument[5])/float(argument[7])
        K3 = float(argument[9])/float(argument[11])
        K=(K1+K2+K3)/3
        Vo1=Vs(1-K)
        #Step down
        k1 = float(argument[13])/float(argument[15])
        k2 = float(argument[17])/float(argument[19])
        k3 = float(argument[21])/float(argument[23])
        k=(k1+k2+k3)/3
        vs=1.3
        vo1 = k*vs
        print(json.dumps({"Mean":[{"Thus the output responses of Step down & Step up MOSFET based choppers were drawn."}],"Step1":[{"Step up MOSFET based choppers practical": str(Vo1)}],"Step2":[{"Step down MOSFET based choppers practical": str(vo1)}]}))

    def SINGLE_PHASE_PWM_INVERTER(self):
        argument = self.arg[0:]
        T1 = float(argument[3])+float(argument[4])
        T2 = float(argument[8])+float(argument[9])
        T3 = float(argument[13])+float(argument[14])
        T=(T1+T2+T3)/3
        print(json.dumps({"Mean":[{"Thus the output waveform for IGBT inverter (PWM) was obtained."}],"Step1":[{"Time": str(T)}]}))
   
    def THREE_PHASE_PWM_INVERTER(self):
        argument = self.arg[0:]
        T1 = float(argument[3])+float(argument[4])
        T2 = float(argument[7])+float(argument[8])
        T3 = float(argument[11])+float(argument[12])
        T=(T1+T2+T3)/3
        print(json.dumps({"Mean":[{"Thus the output waveform for IGBT inverter (PWM) was obtained."}],"Step1":[{"Time": str(T)}]}))
    def AC_VOLTAGE_CONTROLLER(self):
        argument = self.arg[0:]
        R1 = float(argument[17])/float(argument[16])
        R2 = float(argument[20])/float(argument[19])
        R3 = float(argument[23])/float(argument[22])
        R=((R1+R2+R3)/3)*100
        print(json.dumps({"Mean":[{"Thus the operation and performance of the single phase AC voltage control using TRIAC is done and output Verified."}],"Step1":[{"Regulation": str(R)}]}))
    def SWITCHED_MODE_POWER_CONVERTER(self):
        argument = self.arg[0:]
        R1 = float(argument[2])/float(argument[1])
        R2 = float(argument[5])/float(argument[4])
        R3 = float(argument[8])/float(argument[7])
        R=((R1+R2+R3)/3)*100
        print(json.dumps({"Mean":[{"Thus the operation and performance of the Switched mode power converter output Verified."}],"Step1":[{"Regulation": str(R)}]}))