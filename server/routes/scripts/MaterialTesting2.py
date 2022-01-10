import json
import math

class MT2:
    def __init__(self, arg):
        self.arg = arg

    def Gravity(self):
        argument = self.arg[0:]
        G = (float(argument[2]) - float(argument[1]))/((float(argument[2]) - float(argument[1])) - (float(argument[3]) - float(argument[4])) * 0.79)
        print(json.dumps({"gravity":[{"Specific gravity of cement" : str(G)}]}))

    def Fine_aggregate(self):
        argument = self.arg[0:]
        G = (float(argument[2]) - float(argument[1]))/((float(argument[4]) - float(argument[1])) - (float(argument[3]) - float(argument[2])))
        print(json.dumps({"gravity":[{"Specific gravity of fine aggregate" : str(G)}]}))

    def coarse_aggregate(self):
        argument = self.arg[:]
        G = (float(argument[2]) - float(argument[1]))/((float(argument[4]) - float(argument[1])) - (float(argument[3]) - float(argument[2])))
        print(json.dumps({"gravity":[{"Specific gravity of coarse aggregate" : str(G)}]}))

    def Slump(self):
        argument = self.arg[:]
        G = float(argument[1])
        print(json.dumps({"Consistency":[{"The slump value of the concrete is " : str(G)+"mm"}]}))

    def Bulk(self):
        argument = self.arg[:]
        h1 = float(argument[1])
        h2 = float(argument[2])
        B = ((h1-h2)/h2)*100
        print(json.dumps({"bulk":[{"Bulking of a given sample of fine aggregate is found to be " : str(B) + "minutes"}]}))

    def Size_aggregate(self):
        argument = self.arg[:]
        #print(argument)
        C1 = (float(argument[2]) - float(argument[1]))
        C2 = (float(argument[6]) - float(argument[5]))
        C3 = (float(argument[10]) - float(argument[9]))
        C4 = (float(argument[14]) - float(argument[13]))
        C5 = (float(argument[18]) - float(argument[17]))
        C6 = (float(argument[22]) - float(argument[21])) 
    
        F1 = (100 - float(argument[4]))
        F2 = (100 - float(argument[8]))
        F3 = (100 - float(argument[12]))
        F4 = (100 - float(argument[16]))
        F5 = (100 - float(argument[20]))
        F6 = (100 - float(argument[24]))
    
        F = (float(argument[4]) + float(argument[8]) + float(argument[12]) + float(argument[16]) + float(argument[20])+ float(argument[24]))/100

        print(json.dumps({"gravity":[{"The finess modulus of coarse aggregate" : str(F)}]}))

    def particle_aggregate(self):
        argument = self.arg[:]
        E1 = (float(argument[1]) + float(argument[1]))
        E2 = E1 + float(argument[3])
        E3 = E2 + float(argument[5])
        E4 = E3 + float(argument[7])
        E5 = E4 + float(argument[9])
        E6 = E5 + float(argument[11]) 
    
        R1 = E1/10
        R2 = E2/10
        R3 = E3/10
        R4 = E4/10
        R5 = E5/10
        R6 = E6/10
    
        F = (R1+R2+R3+R4+R5+R6)/100
        print(json.dumps({"gravity":[{"The finess modulus of a given sample of fine aggregate is " : str(F)}]}))

    def Consistency(self):
        argument = self.arg[:]
        G = float(argument[1])
        print(json.dumps({"Consistency":[{"The normal consistency of a given sample if cement is " : str(G)}]}))

    def Setting_time(self):
        argument = self.arg[:]
        I = float(argument[4])
        F = float(argument[7])
        print(json.dumps({"initial":[{"The initial setting time of the cement sample is found to be " : str(I) + "minutes"}], "final":[{"The final setting time of the cement sample is found to be " : str(F) + "minutes"}]}))

    def Vee_Bee(self):
        argument = self.arg[:]
        G = float(argument[1])
        print(json.dumps({"Consistency":[{"The consistency of the concrete is " : str(G)+ "Seconds"}]}))

    def compaction(self):
        argument = self.arg[:]
        G = (float(argument[2])-float(argument[1]))/(float(argument[3])-float(argument[1]))
        print(json.dumps({"Compaction":[{"The compaction factor of the given sample of concrete is " : str(G)}]}))
    def compression(self):
        argument = self.arg[:]
        g = (float(argument[1])+float(argument[2])+float(argument[3]))/3
        G = float("{:.2f}".format(g))
        print(json.dumps({"Compression":[{"The compressive strength of cement concrete is " : str(G)+"Mpa"}]}))

    def Flexural(self):
        argument = self.arg[:]
        G = (((float(argument[4])*0.5)*float(argument[1]))/(float(argument[2])*float(argument[3])**2))*1000
        print(json.dumps({"strenght":[{"The strength of concrete is " : str(G)+"N/mm2"}]}))

