#Import library
import json
import math

class EVS:
    def __init__(self, arg):
        self.arg = arg

    def total_solids(self):
        argument = self.arg[0:]
        TS = ((float(argument[2])-float(argument[1]))/float(argument[3]))*10**6
        print(json.dumps({"hardness":[{"Total solids present in the given water sample" : str(TS) + " mg/L" }]}))

    def alkalinity(self):
        argument = self.arg[0:]
        #print(argument)
        P = (float(argument[2])+float(argument[6]))/2

        C = (float(argument[4])+float(argument[8]))/2
        M2 = ((P*0.05)/1)*(2/C)
        P1 = (float(argument[10])+float(argument[15]))/2
        C1 = (float(argument[13])+float(argument[18]))/2
        M1 = ((P1*M2)/1)*(1/C1)
        co3 = M1*60*1000

        print(json.dumps({"alkalinity":[{"The alkalinity of given water sample" : str(co3) + " mg/L" }]}))


    def chloride(self):
        argument = self.arg[0:]
        #print(argument)
        P = ( float(argument[2])+ float(argument[6]))/2
        B = ( float(argument[4])+ float(argument[8]))/2
        A = (float(argument[12])+float(argument[16]))/2
        Acl = ((A-B)*0.0172*35.45*1000)/P
        print(json.dumps({"chloride":[{"Amount of chloride present in the given sample" : str(Acl) + " mg/L" }]}))
   
    def total_hardness(self):
        argument = self.arg[0:]
        C1 = (float(argument[4])+float(argument[8]))/2
        C2 = (float(argument[12])+float(argument[16]))/2
        V = (C2/C1)*1000

        print(json.dumps({"hardness":[{"Total hardness of the given sample" : str(V) + " mg/L" }]}))


    def chlorine(self):
        argument = self.arg[0:]
        #print(argument)
        P = (float(argument[2])+float(argument[6]))/2
        B = (float(argument[4])+float(argument[8]))/2
        M2 = (((P*0.002)/1)*(6/B))
        A = (float(argument[12])+float(argument[16]))/2
        Acl = ((35.45)*A*M2*1000)/P
        print(json.dumps({"chlorine":[{"Amount of residual chlorine present in the given sample" : str(Acl) + " mg/L" }]}))

    def dissolved_oxygen(self):
        argument = self.arg[0:]
        #print(argument)
        P = ( float(argument[2])+ float(argument[6]))/2
        B = ( float(argument[4])+ float(argument[8]))/2
        M2 = (P*0.002/1)*(6/B)
        A = (float(argument[12])+float(argument[16]))/2
        Acl = (8*A*M2*1000)/P
        print(json.dumps({"dissolved":[{"Concentration of dissolved oxygen present in the given sample" : str(Acl) + " mg/L" }]}))





