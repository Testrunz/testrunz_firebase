import json
import math


class POWELC:
    def __init__(self, arg):
        self.arg = arg
    def Gate_Pulse_Generation(self):
        argument = self.arg[0:]
        #print(argument)
        Eff1 = (float(argument[10]/float(argument[10])* 100
        Eff2 = (float(argument[10]/float(argument[10])* 100
        Eff3 = (float(argument[10]/float(argument[10])* 100
        Eff4 = (float(argument[10]/float(argument[10])* 100
        Eff5 = (float(argument[10]/float(argument[10])* 100
        Eff6 = (float(argument[10]/float(argument[10])* 100
        
        Eff = (Eff1 + Eff2 + Eff3 + Eff4 + Eff5 + Eff6)/6

                      

        Vfl = 115
        Reg1 = ((Vfl-float(argument[10]))/Vfl)* 100
        Reg2 = ((Vfl-float(argument[10]))/Vfl)* 100
        Reg3 = ((Vfl-float(argument[10]))/Vfl)* 100
        Reg4 = ((Vfl-float(argument[10]))/Vfl)* 100
        Reg5 = ((Vfl-float(argument[10]))/Vfl)* 100
        Reg6 = ((Vfl-float(argument[10]))/Vfl)* 100
        
        Reg = (Reg1 + Reg2 + Reg3 + Reg4 + Reg5 + Reg6)/6
                      
        #Armature_Resistance Ra table2
        Ra1 = float(argument[10])/float(argument[10])
        Ra2 = float(argument[10])/float(argument[10])
        Ra3 = float(argument[10])/float(argument[10])
        Ra4 = float(argument[10])/float(argument[10])
        Ra5 = float(argument[10])/float(argument[10])
                      
        Ra = (Ra1 + Ra2 + Ra3 + Ra4 + Ra5)/5
        print("Mean=",Ra, 'ohm')
        print(json.dumps({"Mean":[{"The Efficiency is" : str(Eff)}], "Mean":[{"The Regularity is" : str(Reg) + " N"}], "Mean":[{"The Armature Resistance is" : str(Ra) + " Ohm"}]}))

                  

                  
     def SCR_and_TRIAC(self):
        argument = self.arg[0:]
        #Armature_Resistance Ra
         #Torque
        T1 = 9.81*((float(argument[10])-float(argument[10]))+2)*0.0986
        T2 = 9.81*((float(argument[10])-float(argument[10]))+2)*0.0986
        T3 = 9.81*((float(argument[10])-float(argument[10]))+2)*0.0986
        T4 = 9.81*((float(argument[10])-float(argument[10]))+2)*0.0986
        T5 = 9.81*((float(argument[10])-float(argument[10]))+2)*0.0986
                      
        #input
        IP1 = float(argument[10]) * float(argument[10])
        IP2 = float(argument[10]) * float(argument[10])
        IP3 = float(argument[10]) * float(argument[10])
        IP4 = float(argument[10]) * float(argument[10])
        IP5 = float(argument[10]) * float(argument[10])

            #output
        OP1 = (2*math.pi*float(argument[10])*float(argument[10]))/60
        OP2 = (2*math.pi*float(argument[10])*float(argument[10]))/60
        OP3 = (2*math.pi*float(argument[10])*float(argument[10]))/60
        OP4 = (2*math.pi*float(argument[10])*float(argument[10]))/60
        OP5 = (2*math.pi*float(argument[10])*float(argument[10]))/60

        #Eff
        Eff1 = (OP1/IP1)*100
        Eff2 = (OP2/IP2)*100
        Eff3 = (OP3/IP3)*100
        Eff4 = (OP4/IP4)*100
        Eff5 = (OP5/IP5)*100
        Eff = (Eff1 + Eff2 + Eff3 + Eff4 + Eff5)/5



        print(json.dumps({"Mean":[{"The Three Phase Two Wattmeter is" : str(Eff)}]}))

                      
     def fMOSFET_and_IGBT(self):
        argument = self.arg[0:]
        #Armature_Resistance Ra
        print(json.dumps({"Mean":[{"The SPEED CONTROL experiment is sucessfully completed"}]}))

                      
     def half_controlled_converter(self):
        argument = self.arg[0:]
        #Armature_Resistance Ra
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

                     
     def  fully_controlled_converter(self):
        argument = self.arg[0:]
        #Armature_Resistance Ra
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

                      
    def MOSFET_based_choppers(self):
        argument = self.arg[0:]
        #Armature_Resistance Ra
                       
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

