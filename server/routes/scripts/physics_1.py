import json
import math

class TE2:
    def __init__(self, arg):
        self.arg = arg
    def Port_diagram(self):
        argument = self.arg[1:]
        def mean(x,y,z):
            ans = (x+y+z)/3
            return ans
        IPO = mean(float(argument[1]),float(argument[2]),float(argument[3]))
        IPC = mean(float(argument[4]),float(argument[5]),float(argument[6]))
        EPO = mean(float(argument[7]),float(argument[8]),float(argument[9]))
        EPC = mean(float(argument[10]),float(argument[11]),float(argument[12]))
        TPO = mean(float(argument[13]),float(argument[14]),float(argument[15]))
        IPC_Af = mean(float(argument[16]),float(argument[17]),float(argument[18]))
        print(json.dumps({"Result":[{"Port Timing Diagram":"The given two stroke engine is studied and the port timing diagram is drawn for the present set of value","IPO before TDC" : str(IPO), "4IPC after TDC": str(IPC), "EPO before BDC ": str(EPO),"EPC after BDC":str(EPC) ,"TPO before BDC":str(TPO),"IPC after BDC":str(IPC_Af)}]}))
    def Valve_diagram(self):
        argument = self.arg[1:]