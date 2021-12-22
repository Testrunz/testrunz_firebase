import json
import math
class MAM:
    def __init__(self, arg):
        self.arg = arg
    def Impact_test_charpy(self):
        argument = self.arg[:]
#got output
        I1 = float(argument[4])/float(argument[3])
        I2 = float(argument[8])/float(argument[7])
        I3 = float(argument[12])/float(argument[11])
        Avg = (I1+I2+I3)/3
        print(json.dumps({"Impact":[{"Charpy impact strength for mild steel":str(Avg)+ " joules/mm2" }]}))


    def Impact_test_diode(self):
        argument = self.arg[:]


        I1 = float(argument[4])/float(argument[3])
        I2 = float(argument[8])/float(argument[7])
        I3 = float(argument[12])/float(argument[11])
        Avg = (I1+I2+I3)/3
        print(json.dumps({"Impact":[{"Izod impact strength for mild steel":str(Avg)+ " joules/mm2" }]}))


    def Erichsen_sheet_metal_test(self):
        argument = self.arg[:]
        A = (float(argument[4])+float(argument[8])+float(argument[12]))/3
        print(json.dumps({"Average":[{"Average Erichsen value for aluminium" : str(A)}]}))
        
    def Hardness_test(self):
        argument = self.arg[:]
        #got output
        BHM1 = (2*float(argument[2]))/((math.pi*float(argument[1]))*(float(argument[1])-(math.sqrt(float(argument[1])**2-float(argument[3])**2))))
        BHM2 = (2*float(argument[5]))/((math.pi*float(argument[4]))*(float(argument[4])-(math.sqrt(float(argument[4])**2-float(argument[6])**2))))
        BHM3 = (2*float(argument[8]))/((math.pi*float(argument[7]))*(float(argument[7])-(math.sqrt(float(argument[7])**2-float(argument[9])**2))))
        BHM = (BHM1+BHM2+BHM3)/3
        BH1 = (2*float(argument[11]))/((math.pi*float(argument[10]))*(float(argument[10])-(math.sqrt(float(argument[10])**2-float(argument[12])**2))))
        BH2 = (2*float(argument[14]))/((math.pi*float(argument[13]))*(float(argument[13])-(math.sqrt(float(argument[13])**2-float(argument[15])**2))))
        BH3 = (2*float(argument[17]))/((math.pi*float(argument[16]))*(float(argument[16])-(math.sqrt(float(argument[16])**2-float(argument[18])**2))))
        BH = (BH1+BH2+BH3)/3
        B1 = (2*float(argument[20]))/((math.pi*float(argument[19]))*(float(argument[19])-(math.sqrt(float(argument[19])**2-float(argument[21])**2))))
        B2 = (2*float(argument[23]))/((math.pi*float(argument[22]))*(float(argument[22])-(math.sqrt(float(argument[22])**2-float(argument[24])**2))))
        B3 = (2*float(argument[26]))/((math.pi*float(argument[25]))*(float(argument[25])-(math.sqrt(float(argument[25])**2-float(argument[27])**2))))
        B = (B1+B2+B3)/3
        print(json.dumps({"Average":[{"Brinell hardness number for Copper" : str(BHM),"Brinell hardness number for Aluminium" : str(BH),"Brinell hardness number for Cast iron" : str(B) }]}))
        
    def Rock_well_hardness(self):
        argument = self.arg[0:]
        #print(argument)got output
        C1 = (float(argument[3])+float(argument[6])+float(argument[9]))/3
        C2 = (float(argument[12])+float(argument[15])+float(argument[18]))/3
        C3 = (float(argument[21])+float(argument[24])+float(argument[27]))/3
        print(json.dumps({"length":[{"Rock well hardness number in copper" : str(C1)}], "breadth":[{"Rock well hardness number in copper" : str(C2) }], "width":[{"Rock well hardness number in cast iron" : str(C3)}]}))

    def Tension_test(self):
        argument = self.arg[0:]
        #gotoutput
        import math 
        A0 = (math.pi/4)*float(argument[1])**2
        S = float(argument[6])/A0
        S1 = float(argument[7])/A0
        E = ((float(argument[4])-float(argument[2]))/float(argument[2]))*100
        A1 = (math.pi/4)*float(argument[5])**2
        A = ((A0-A1)/A0)*100

        #Linear strain
        LS1 = (float(argument[4])-float(argument[2]))/float(argument[2])
        #print(f'LS1: {LS1}')
        LS2 = (float(argument[1])-float(argument[5]))/float(argument[5])
        #print(f'LS2: {LS2}')

        print(json.dumps({"Tes":[{"Ultimate tensile strength" : str(S) }], "Test":[{"Yield distance" : str(S1)}],"N1":[{"Percentage reduction in cross-section area":str(A)}],"N2":[{"Percentage elongation":str(E)}],"N3":[{"Lateral and linear strain":str(LS2)}],"N4":[{"Lateral and linear stress":str(LS1) }]}))
 
    def Annealing(self):
        print(json.dumps({"answer":[{"result":"Thus the given specimen was annealed and its hardness was studied"}]}))        #Thus the given specimen was annealed and its hardness was studied.
    def Normalizing(self):
        print(json.dumps({"answer":[{"result":"Thus the normalizing was done on the steel and properties were studied"}]}))

    def Heat(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the heat treatment process was performed"}]}))
    
        #Thus the heat treatment process was performed.

    def Hardening(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the heat treatment process was performed"}]}))

    def Microstructure(self):
        argument = self.arg[0:]
        #print(argument)
        R = str(argument[1])
        print(json.dumps({"answer":[{"Thus the given specimen was polished and the microstructure of the given metal is ":str(R)}]}))
    
    def Metallurgical(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the Metallurgical Microscope is studied."}]}))
 
    def Microscopic(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the specimen preparation has been done to study its structure under microscope and metallographic result haven been obtained"}]}))
    def Hardenability(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Then the hardness test was done on mild steel and a graph was drawn."}]}))
    def Etchants(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the preparation and application of the etchants are studied."}]}))