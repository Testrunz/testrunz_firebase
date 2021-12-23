import json

class EL1:
    def __init__(self, arg):
        self.arg = arg

    def Triac(self):
        argument = self.arg[0:]
        FV = float(argument[21])
        RV = float(argument[22])
        print(json.dumps({"answer":[{"Result":"Thus the V-I characteristics of TRIAC was obtained and graph was drawn.","Break over voltage in forward direction of TRIAC (VBO)":FV,"Break over voltage in forward direction of TRIAC (VBO)":RV}]}))

    def CRO(self):
        argument = self.arg[0:]
        #Peak voltag
        PV1 = float(argument[1])*float(argument[2])
        PV2 = float(argument[3])*float(argument[4])
        PV3 = float(argument[5])*float(argument[6])
        PV4 = float(argument[7])*float(argument[8])
        PV=(PV1+PV2+PV3+PV4)/4
        #Time period
        TP1 = float(argument[9])*float(argument[10])
        TP2 = float(argument[11])*float(argument[12])
        TP3 = float(argument[13])*float(argument[14])
        TP4 = float(argument[15])*float(argument[16])
        #Frequency
        F1 = 1/TP1
        F2 = 1/TP2
        F3 = 1/TP3
        F4 = 1/TP4
        F=(F1+F2+F3+F4)/4
        print(json.dumps({"answer":[{"Result":"Thus the Amplitude and frequency Measurement for different waveforms is obtained","Amplitude":PV,"Frequency":F}]}))

    def PN_Juction(self):
        print(json.dumps({"answer":[{"Result":"The static and dynamic resistances of the PN Junction Diode are calculated from the forward and reverse bias Characteristics."}]}))

    def Clipper(self):
        print(json.dumps({"answer":[{"Result":"Thus the output performance for the clippers and clampers circuit is verified."}]}))        
    
    def zener(self):
        argument = self.arg[0:]
        V = float(argument[21])
        print(json.dumps({"answer":[{"Result":"Forward and Reverse Bias characteristics for a zener diode are observed and the breakdown voltage   of zener  diode  is  obtained. ","Breakdown voltage":V}]}))
    
    def Bias(self):
        print(json.dumps({"answer":[{"Result":"Thus the various biasing circuits has been designed and tested successfully."}]})) 
    
    def SCR(self):
        print(json.dumps({"answer":[{"Result":"The Characteristics of SCR was studied and the graphs were plotted."}]})) 
    
    def CB(self):
        print(json.dumps({"answer":[{"Result":"Thus the input and output characteristics of the bipolar junction  transistor in Common Base configuration is obtained."}]})) 

    def CE(self):
        print(json.dumps({"answer":[{"Result":"Thus the input and output characteristics of the bipolar junction transistor in  Common Emitter configuration is obtained."}]})) 

    def JFET(self):
        print(json.dumps({"answer":[{"Result":"Thus the  Drain  & Transfer  characteristics  of given  FET is Plotted. "}]}))         
    
    def UJT(self):
        print(json.dumps({"answer":[{"Result":"1. Thus the characteristics of given UJT was Plotted & its intrinsic standoff Ratio = "}]}))         
