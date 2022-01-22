import json
import math
class EE:
    def __init__(self, arg):
        self.arg = arg
    def single_trf(self):
        argument = self.arg[:]
        Ra1 = float(argument[2])*float(argument[5])
        Ra2 = float(argument[9])*float(argument[12])
        Ra3 = float(argument[16])*float(argument[19])
        Ra4 = float(argument[23])*float(argument[26])
        Ra5 = float(argument[30])*float(argument[33])
        E1 = (Ra1/float(argument[7]))*100
        E2 = (Ra2/float(argument[14]))*100
        E3 = (Ra3/float(argument[21]))*100
        E4 = (Ra4/float(argument[28]))*100
        E5 = (Ra5/float(argument[35]))*100
        R1 = (1500-float(argument[1]))/float(argument[1])
        R2 = (1500-float(argument[8]))/float(argument[8])
        R3 = (1500-float(argument[15]))/float(argument[15])
        R4 = (1500-float(argument[22]))/float(argument[22])
        R5 = (1500-float(argument[29]))/float(argument[29])
        E=(E1+E2+E3+E4+E5)/5
        R=(R1+R2+R3+R4+R5)/5
        print(json.dumps({"answer":[{"result":"Thus the efficiency and regulation of a transformer is predetermined by conducting open circuit test and short circuit test and the equivalent circuit is drawn.","Efficiency":str(E),"Regulation":str(R)}]}))
