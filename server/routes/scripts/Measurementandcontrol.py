import json
import math as m

class MAC:
    def __init__(self, arg):
        self.arg = arg[0:]
    def Single(self):
    	argument = self.arg[0:]
    	TE1 = (float(argument[4]) * float(argument[6]))/(60*60*1000)
    	TE2 = (float(argument[10]) * float(argument[12]))/(60*60*1000)
    	TE3 = (float(argument[16]) * float(argument[18]))/(60*60*1000)
    	TE4 = (float(argument[22]) * float(argument[24]))/(60*60*1000)
    	TE=(TE1+TE2+TE3+TE4)/4
    	RE1=60/(float(argument[1]) * float(argument[2]))
    	RE2=60/(float(argument[7]) * float(argument[8]))
    	RE3=60/(float(argument[13]) * float(argument[14]))
    	RE4=60/(float(argument[19]) * float(argument[20]))
    	RE=(RE1+RE2+RE3+RE4)/4
    	Error = ((TE-RE)/RE)*100
    	print(json.dumps({"length":[{"True Energy" : str(TE)}], "breadth":[{"Record Energy" : str(RE)}], "breadth":[{"Error" : str(Error)}]}))
    def Network(self):
    	argument = self.arg[0:]
    	R1 = (float(argument[2]) / float(argument[1]))
    	R2 = (float(argument[4]) / float(argument[3]))
    	R=(R1+R2)/2
    	print(json.dumps({"length":[{"Thus the Thevenin's and Superposition theorem have been verified theoretically and practically."}], "breadth":[{"Ans" : str(R)}]}))
    
    def Bridge(self):
    	argument = self.arg[0:]
    	R1 = (float(argument[1]) + float(argument[2]) +float(argument[3]))/3
    	R2 = (float(argument[5]) + float(argument[6]) +float(argument[7]))/3
    	R3 = (float(argument[9]) + float(argument[10]) +float(argument[11]))/3
    	R4 = (float(argument[13]) + float(argument[14]) +float(argument[15]))/3
    	R5 = (float(argument[17]) + float(argument[18]) +float(argument[19]))/3
    	R=(R1+R2+R3+R4+R5)/5
    	K1= (float(argument[21]) * float(argument[23])) /float(argument[22])
    	K2= (float(argument[24]) * float(argument[26])) /float(argument[25])
    	K3= (float(argument[27]) * float(argument[29])) /float(argument[28])
    	K4= (float(argument[30]) * float(argument[32])) /float(argument[31])
    	K5= (float(argument[33]) * float(argument[35])) /float(argument[34])
    	RX1= K1*0.1
    	RX2= K2*0.1
    	RX3= K3*0.1
    	RX4= K4*0.1
    	RX5= K5*0.1
    	Rx=(RX1+RX2+RX3+RX4+RX5)/5
    	print(json.dumps({"length":[{"Thus the values of the medium and low resistance are measured using Wheatstone and Kelvin’s double bridge."}], "breadth":[{"Observed Resistance in Ohms" : str(R)}], "bread":[{"Set value RX" : str(Rx)}]}))
    def VOLTMETER(self):
    	argument = self.arg[0:]
    	R1 = (float(argument[1]) / float(argument[2]))
    	R2 = (float(argument[3]) / float(argument[4]))
    	R3 = (float(argument[5]) / float(argument[6]))
    	R4 = (float(argument[7]) / float(argument[8]))
    	R5 = (float(argument[9]) / float(argument[10]))
    	R6 = (float(argument[11]) / float(argument[12]))
    	R =(R1+R2+R3+R4+R5+R6)/6
        E1 = ((float(argument[14]) - float(argument[15])) /float(argument[15]))*100
        E2 = ((float(argument[17]) - float(argument[18])) /float(argument[18]))*100
        E3 = ((float(argument[20]) - float(argument[21])) /float(argument[21]))*100
        E4 = ((float(argument[23]) - float(argument[24])) /float(argument[24]))*100
        E5 = ((float(argument[26]) - float(argument[27])) /float(argument[27]))*100
        E6 = ((float(argument[29]) - float(argument[30])) /float(argument[30]))*100
        E=(E1+E2+E3+E4+E5+E6)/6
    	print(json.dumps({"length":[{"Thus the range of voltmeter and ammeter is extended to the desired value."}], "breadth":[{"Resistance" : str(R)}], "bread":[{"Error Percentage" : str(E)}]}))
    
    def VOLTAGE(self):
    	print(json.dumps({"answer":[{"result":"Thus the characteristics of signal converter circuits using grounded load and floating load is determined."}]}))

    def INSTRUMENTATION(self):
    	argument = self.arg[0:]
    	Vin=0.2
    	dB1 = 20*math.log((float(argument[2])*0.2)/Vin)
    	dB2 = 20*math.log((float(argument[4])*0.2)/Vin)
    	dB3 = 20*math.log((float(argument[6])*0.2)/Vin)
    	dB4 = 20*math.log((float(argument[8])*0.2)/Vin)
    	dB5 = 20*math.log((float(argument[10])*0.2)/Vin)
    	dB6 = 20*math.log((float(argument[12])*0.2)/Vin)
    	dB7 = 20*math.log((float(argument[14])*0.2)/Vin)
    	dB= (dB1+dB2+dB3+dB4+dB5+dB6+dB7)/7
    	vin=0.3
    	DB1 =20*math.log((float(argument[16])*0.2)/Vin)
    	DB2 =20*math.log((float(argument[18])*0.2)/Vin)
    	DB3 =20*math.log((float(argument[20])*0.2)/Vin)
    	DB4 =20*math.log((float(argument[22])*0.2)/Vin)
    	DB5 =20*math.log((float(argument[24])*0.2)/Vin)
    	DB=(DB1+DB2+DB3+DB4+DB5)/5
    	print(json.dumps({"length":[{"Thus the frequency response characteristics of an instrumentation amplifierhas been obtained & plotted."}], "breadth":[{"Gain In DB from table 1" : str(dB)}], "bread":[{"Gain In DB from table 2" : str(DB)}]}))
    def TRANSFER(self):
    	argument = self.arg[0:]
    	R1 = (float(argument[1]) / float(argument[2]))
		R2 = (float(argument[3]) / float(argument[4]))
		R3 = (float(argument[5]) / float(argument[6]))
		R4 = (float(argument[7]) / float(argument[8]))
		R5 = (float(argument[9]) / float(argument[10]))
		Ra=(R1+R2+R3+R4+R5)/5
		Z1=(float(argument[11]) / float(argument[12]))
		Z2=(float(argument[13]) / float(argument[14]))
		Z3=(float(argument[15]) / float(argument[16]))
		Z4=(float(argument[17]) / float(argument[18]))
		Z5=(float(argument[19]) / float(argument[20]))
		Za=(Z1+Z2+Z3+Z4+Z5)/5
		r=0.25
		T1=9.81*r*(float(argument[21]) - float(argument[22]))
		T2=9.81*r*(float(argument[24]) - float(argument[25]))
		T3=9.81*r*(float(argument[27]) - float(argument[28]))
		T4=9.81*r*(float(argument[30]) - float(argument[31]))
		Ka=(T1+T2+T3+T4)/4
		V = (float(argument[33]) + float(argument[36]) +float(argument[39])+float(argument[42]))/4
		Eb1=V-(float(argument[34])*Ra)
		Eb2=V-(float(argument[37])*Ra)
		Eb3=V-(float(argument[40])*Ra)
		Eb4=V-(float(argument[43])*Ra)
		W1=(2*m.pi*float(argument[35]))/60
		W2=(2*m.pi*float(argument[38]))/60
		W3=(2*m.pi*float(argument[41]))/60
		W4=(2*m.pi*float(argument[44]))/60
		W=(W1+W2+W3+W4)/4
		Kb=V/W
		print(json.dumps({"length":[{"Thus  the  transfer  function  of  armature  controlled  DC  shunt  motor  was determined."}], "breadth":[{"Ka" : str(Ka)}], "bread":[{"Kb" : str(Kb)}]}))
    def LDR(self):
    	print(json.dumps({"answer":[{"result":"Thus the V-I characteristics of LDR was drawn for various  illuminations level at constant supply voltage and various and supply voltage as constant illumination level."}]}))
    def THERMOCOUPLE(self):
    	print(json.dumps({"answer":[{"result":"Thus the characteristics of temperature transducer using RTD and thermocouple have been studied and plotted."}]}))
    def THERMOCOUPLE(self):
    	print(json.dumps({"answer":[{"result":"Thus the ratio between V and F is compared with theoretical value and it is verified."}]}))
    def DISPLACEMENT(self):
    	argument = self.arg[0:]
    	R1 = (float(argument[2]) -float(argument[3]))
		R2 = (float(argument[5]) - float(argument[6]))
		R3 = (float(argument[8]) - float(argument[9]))
		R4 = (float(argument[11]) - float(argument[12]))
		R5 = (float(argument[14]) - float(argument[15]))
		Ra=(R1+R2+R3+R4+R5)/5
		print(json.dumps({"length":[{"Thus the characteristics of Linear Variable Displacement Transducer  are studied and plotted."}], "breadth":[{"V" : str(R)}]}))
    def Three(self):
    	argument = self.arg[0:]
    	TE1 = (float(argument[4]) * float(argument[6]))/(60*60*1000)
    	TE2 = (float(argument[10]) * float(argument[12]))/(60*60*1000)
    	TE3 = (float(argument[16]) * float(argument[18]))/(60*60*1000)
    	TE4 = (float(argument[22]) * float(argument[24]))/(60*60*1000)
    	TE5 = (float(argument[28]) * float(argument[30]))/(60*60*1000)
    	TE=(TE1+TE2+TE3+TE4+TE5)/5
    	RE1=60/(float(argument[1]) * float(argument[2]))
    	RE2=60/(float(argument[7]) * float(argument[8]))
    	RE3=60/(float(argument[13]) * float(argument[14]))
    	RE4=60/(float(argument[19]) * float(argument[20]))
    	RE5=60/(float(argument[25]) * float(argument[26]))
    	RE=(RE1+RE2+RE3+RE4+RE5)/5
    	Error = ((TE-RE)/RE)*100
    	print(json.dumps({"length":[{"The  three phase meters are calibrated using wattmeter and the respective graphs are drawn."}], "True":[{"True Energy" : str(TE)}], "breadth":[{"Record Energy" : str(RE)}], "breadth":[{"Error" : str(Error)}]}))
        