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
        circumference = 1250
        Angle1 = float(argument[1])*360 / circumference
        Angle2 = float(argument[2])*360 / circumference
        Angle3 = float(argument[3])*360 / circumference
        Angle4 = float(argument[4])*360 / circumference
        print(json.dumps({"Result":[{"Value Timing Diagram":"The given four stroke compressed ignition engine is studied and the value timing diagram is drawn for the present set of value","Angle_1" : float(argument[1]), "Angle_2": float(argument[2]), "Angle_3 ": float(argument[3]),"Angle_4":float(argument[4])}]}))
    def Single_petrol(self):
        argument = self.arg[1:]
        a = float(argument[1])/float(argument[2])
        print(json.dumps({"Result":[{"Port Timing Diagram":str(a)}]}))
    #     def mass(a,b):
    #         return 1000*0.78*(a/1000)**2*(b/100)
    #     def RE(a,b,c):
    #         return a*4.178*(b-c)/1500
    #     def Work(a,b):
    #         return 3600*10/(a*b)
    #     def cop(a,b):
    #         return(a/b)
    #     def h(a,b,c,d):
    #         return a+b/(c-d)
    #     mass1 = mass(float(argument[1]),float(argument[15]))
    #     mass2 = mass(float(argument[1]),float(argument[28]))
    #     mass3 = mass(float(argument[1]),float(argument[41]))
    #     RE1 = RE(mass1,float(argument[3]),float(argument[4]))
    #     RE2 = RE(mass2,float(argument[16]),float(argument[17]))
    #     RE3 = RE(mass3,float(argument[29]),float(argument[30]))
    #     W1=Work(float(argument[2]),float(argument[14]))
    #     W2=Work(float(argument[2]),float(argument[27]))
    #     W3=Work(float(argument[2]),float(argument[40]))
    #     mcop=(cop(RE1,W1)+cop(RE2,W2)+cop(RE3,W3))/3
    #     h1=h(420.44,1070,float(argument[6]),float(argument[7]))
    #     h4=h(393.715,891.9,float(argument[9]),float(argument[8]))
    #     h3=259.35
    #     cop_theo=(h1-h3)/(h1-h4)
    #     print(json.dumps({"Result":[{"The performance test was conducted in refrigeration test rig and the result are : The co-efficient of performance of refrigeration":str(mcop),"The Theoritical value of COP":str(cop_theo)}]}))
    # def heat_4stroke(self):
    #     argument = self.arg[0:]
        
    #     def BP(a):
    #         return 11.22*a/60000
    #     def TFC(a):
    #         return 29790/(a*1000)
    #     def heat_io(a):
    #         return a*0.0042
    #     def eq_uw(a):
    #         return a*3600
    #     def per_eq_uw(a,b):
    #         return a*100/b
    #     def Qw(a):
    #         return 150408*(2/a)
    #     def Ha(a):
    #         return (a*10)/1.23
    #     def Va(a):
    #         return math.sqrt(19.62*a)
    #     def Ma(a):
    #         return a*1.23
    #     def Mg(a,b):
    #         return a+b
    #     def heat_egas(a):
    #         return a*32.654
    #     def veff(a,b,c,d,e):
    #         t=0.64*0.785*(a/100)**2*b
    #         d=(c/100)*0.785*(d)**2*(e/120)
    #         return t / d
    #     def unacc_loss(a,b,c,d):
    #         return a-(b+c+d)
    #     BP1 = BP(float(argument[8]))
    #     BP2 = BP(float(argument[14]))
    #     BP3 = BP(float(argument[20]))
    #     BP4 = BP(float(argument[26]))
    #     BP5 = BP(float(argument[32]))
    #     TFC1= TFC(float(argument[9]))
    #     TFC2= TFC(float(argument[15]))
    #     TFC3= TFC(float(argument[21]))
    #     TFC4= TFC(float(argument[27]))
    #     TFC5= TFC(float(argument[33]))
    #     heat_io1 = heat_io(TFC1)
    #     heat_io2 = heat_io(TFC2)
    #     heat_io3 = heat_io(TFC3)
    #     heat_io4 = heat_io(TFC4)
    #     heat_io5 = heat_io(TFC5)
    #     eq_uw1= eq_uw(BP1)
    #     eq_uw2= eq_uw(BP2)
    #     eq_uw3= eq_uw(BP3)
    #     eq_uw4= eq_uw(BP4)
    #     eq_uw5= eq_uw(BP5)
    #     per_eq_uw1=per_eq_uw(eq_uw1,heat_io1)
    #     per_eq_uw2=per_eq_uw(eq_uw1,heat_io2)
    #     per_eq_uw3=per_eq_uw(eq_uw1,heat_io3)
    #     per_eq_uw4=per_eq_uw(eq_uw1,heat_io4)
    #     per_eq_uw5=per_eq_uw(eq_uw1,heat_io5)
    #     Qw1=Qw(float(argument[36]))
    #     Qw2=Qw(float(argument[41]))
    #     Qw3=Qw(float(argument[46]))
    #     Qw4=Qw(float(argument[51]))
    #     Qw5=Qw(float(argument[56]))
        
      



        

