import json

class PowerEle:
    def __init__(self, arg):
        self.arg = arg
        
    def Gate_Pulse_Generation(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the R, RC &UJT triggering circuit for SCR was constructed and its output waveforms were plotted."}]}))
        
    def CHARACTERISTICS_OF_SCR (self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the Characteristics of SCR and the Output waveforms were obtained."}]}))
        
    def CHARACTERISTICS_OF_TRIAC(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the Characteristics of TRIAC and the Output waveforms were obtained."}]}))
        
        
    def MOSFET_IGBT(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the Characteristics of MOSFET & IGBT were obtained."}]}))
        
        
    def HALF_CONTROLLED(self):
        argument = self.arg[0:]
        Vo1 = float(argument[1])*20
        print(Vo1)
        Vo2 = float(argument[2])*20
        print(Vo2)
        Vo3 = float(argument[3])*20
        print(Vo3)
        Vo4 = float(argument[4])*20
        print(Vo4)
        Vo5 = float(argument[5])*20
        print(Vo5)

        print(json.dumps({"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo1)}] ,"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo2)}] ,"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo3)}] ,"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo4)}] , "Mean":[{"The The Step down and step up MOSFET based choppers are" : str(Vo5)}]}))

        
    def FULLY_CONTROLLED(self):
        argument = self.arg[0:]
        Vo1 = float(argument[1])*20
        print(Vo1)
        Vo2 = float(argument[2])*20
        print(Vo2)
        Vo3 = float(argument[3])*20
        print(Vo3)
        Vo4 = float(argument[4])*20
        print(Vo4)
        Vo5 = float(argument[5])*20
        print(Vo5)


        print(json.dumps({"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo1)}] ,"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo2)}] ,"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo3)}] ,"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo4)}] , "Mean":[{"The The Step down and step up MOSFET based choppers are" : str(Vo5)}]}))

    def MOSFET_BASED_CHOPPERS(self):
        argument = self.arg[0:]
        Vo1 = float(argument[1])*20
        print(Vo1)
        Vo2 = float(argument[2])*20
        print(Vo2)
        Vo3 = float(argument[3])*20
        print(Vo3)
        Vo4 = float(argument[4])*20
        print(Vo4)
        Vo5 = float(argument[5])*20
        print(Vo5)


        print(json.dumps({"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo1)}] ,"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo2)}] ,"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo3)}] ,"Mean":[{"The Step down and step up MOSFET based choppers are" : str(Vo4)}] , "Mean":[{"The The Step down and step up MOSFET based choppers are" : str(Vo5)}]}))


        
    def SINGLE_PHASE_PWM_INVERTER(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the output waveform for IGBT inverter (PWM) was obtained."}]}))

    def THREE_PHASE_PWM_INVERTER(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the output waveform for IGBT inverter (PWM) was obtained."}]}))
        
        
    def AC_VOLTAGE_CONTROLLER(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":"Thus the operation and performance of the single phase AC voltage control using TRIAC is done and output Verified."}]}))
        
        
    def SWITCHED_MODE_POWER_CONVERTER(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Ans":" Thus the output of Switched mode power convertor is obtained."}]}))

 
