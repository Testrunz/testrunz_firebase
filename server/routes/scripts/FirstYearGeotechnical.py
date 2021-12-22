import json
import math

class FirstYGtech:
    def __init__(self, arg):
        self.arg = arg
        
    def UCT(self):
        argument = self.arg[0:]
        A = (math.pi/4)*float(argument[0])**2
        B = (float(argument[1])*9.81)/float(argument[2])

        #Corrected Area
        AC1 = A/(1-float(argument[0]))
        AC2 = A/(1-float(argument[1]))
        AC3 = A/(1-float(argument[2]))
        AC4 = A/(1-float(argument[3]))
        AC5 = A/(1-float(argument[4]))
        AC6 = A/(1-float(argument[5]))
        AC7 = A/(1-float(argument[6]))
        AC8 = A/(1-float(argument[7]))
        AC9 = A/(1-float(argument[8]))
        AC10 = A/(1-float(argument[9]))
        AC11 = A/(1-float(argument[10]))
        AC12 = A/(1-float(argument[11]))
        AC13 = A/(1-float(argument[12]))
        AC14 = A/(1-float(argument[13]))
        AC15 = A/(1-float(argument[14]))
        AC16 = A/(1-float(argument[15]))
        AC17 = A/(1-float(argument[16]))
        AC18 = A/(1-float(argument[17]))

        #stress
        S1 = float(argument[1])/A
        S2 = float(argument[2])/A
        S3 = float(argument[3])/A
        S4 = float(argument[4])/A
        S5 = float(argument[5])/A
        S6 = float(argument[6])/A
        S7 = float(argument[7])/A
        S8 = float(argument[8])/A
        S9 = float(argument[9])/A
        S10 = float(argument[0])/A
        S11 = float(argument[1])/A
        S12 = float(argument[2])/A
        S13 = float(argument[3])/A
        S14 = float(argument[4])/A
        S15 = float(argument[5])/A
        S16 = float(argument[6])/A
        S17 = float(argument[7])/A
        S18 = float(argument[8])/A

        

        tan =(float(argument[0])/float(argument[1]))
        tita = degrees(math.atan(tan))

        phi = (tita-45)*2

        print(json.dumps({"Test":[{"The value of Unconfined compression test is" : str(phi)}]}))
        
        
    def Core_cutter_method(self):
        argument = self.arg[0:]
        Water_content = ((float(argument[0]) - float(argument[1]))/(float(argument[2])-float(argument[3])))*100
        w = Water_content/100

        #Bulk unit weight
        mass = float(argument[4])*9.81
        BUW = mass/float(argument[5])

        # Dry unit weight
        DUW = BUW/(1+w)

        #Void ratio
        G = 2.6
        e = ((G*9.81)/DUW)-1

        # Degree of saturation
        Sr = (G*w)/e

        #porosity
        n = e/(1+e)

        print(json.dumps({"Test":[{"The porosity of Core cutter method is" : str(n)}]}))
        
        
    def Grain_size_analysis(self):
        argument = self.arg[0:]

        #percentage weight of soil retaining
        PW1 = (float(argument[0])/float(argument[8]))*100
        PW2 = (float(argument[1])/float(argument[9]))*100
        PW3 = (float(argument[2])/float(argument[0]))*100
        PW4 = (float(argument[3])/float(argument[1]))*100
        PW5 = (float(argument[4])/float(argument[2]))*100
        PW6 = (float(argument[5])/float(argument[3]))*100
        PW7 = (float(argument[5])/float(argument[4]))*100
        PW8 = (float(argument[6])/float(argument[5]))*100
        PW9 = (float(argument[7])/float(argument[6]))*100

        #Cumulative relative percentage
        CP1 = PW1
        CP2 = CP1+PW2
        CP3 = CP2+PW3
        CP4 = CP3+PW4
        CP5 = CP4+PW5
        CP6 = CP5+PW6
        CP7 = CP6+PW7
        CP8 = CP7+PW8
        CP9 = CP8+PW9

        # find uniform co-efficient
        Cu=float(argument[0])/float(argument[1])

        #Co_efficient of curvature
        Cc=(float(argument[1])**2)/(float(argument[1])*float(argument[2]))

        print(json.dumps({"Test":[{"The Co_efficient of curvature in Grain size analysis is" : str(Cc)}]}))

        
    def Sedimentation_Analysis(self):
        argument = self.arg[0:]

        D = math.sqrt((30*float(argument[0]))/980*(float(argument[1])-float(argument[2])))* math.sqrt(float(argument[3])/float(argument[4]))
        NF = ((100*float(argument[1]))/(float(argument[2])*(float(argument[3])-1)))*(float(argument[4]) - float(argument[5]))

        print(json.dumps({"Test":[{"The output of Sedimentation Analysis is" : str(NF)}]}))
    
    def Permiability_of_hydraaulic_conductivity(self):
        argument = self.arg[0:]
            #average
        t1=(float(argument[0])+float(argument[3])+float(argument[6]))/3
        t2=(float(argument[1])+float(argument[4])+float(argument[7]))/3
        t3=(float(argument[2])+float(argument[5])+float(argument[8]))/3

        #Co-efficient of permibility
        Rs1 = t1*float(argument[0])/(float(argument[3])*float(argument[6])*float(argument[9]))
        Rs2 = t2*float(argument[1])/(float(argument[4])*float(argument[7])*float(argument[0]))
        Rs3 = t3*float(argument[2])/(float(argument[5])*float(argument[8])*float(argument[1]))


        k1 =(((2.3*float(argument[0])*float(argument[1]))/(float(argument[2])*float(argument[3])))*(math.log(float(argument[1])/float(argument[2]))))
        k2 =(((2.3*float(argument[1])*float(argument[2]))/(float(argument[3])*float(argument[4])))*(math.log(float(argument[1])/float(argument[1]))))
        k3 =(((2.3*float(argument[2])*float(argument[4]))/(float(argument[4])*float(argument[4])))*(math.log(float(argument[4])/float(argument[5]))))

        print(json.dumps({"Test":[{"The Permiability of hydraaulic conductivity is" : str(k3)}]}))

        
    def Liquid_and_plastic_limit_final(self):
        argument = self.arg[0:]
        #Water content calculation
        WC1 = ((float(argument[0])-float(argument[6]))/(float(argument[2])-float(argument[8])))*100
        WC2 = ((float(argument[1])-float(argument[7]))/(float(argument[3])-float(argument[9])))*100
        WC3 = ((float(argument[2])-float(argument[8]))/(float(argument[4])-float(argument[0])))*100
        WC4 = ((float(argument[3])-float(argument[9]))/(float(argument[5])-float(argument[1])))*100
        WC5 = ((float(argument[4])-float(argument[0]))/(float(argument[6])-float(argument[2])))*100
        WC6 = ((float(argument[5])-float(argument[1]))/(float(argument[7])-float(argument[3])))*100
        Wl= (WC1+WC2+WC3+WC4+WC5+WC6)/6


        Wc1 = ((float(argument[1])-float(argument[3]))/(float(argument[5])-float(argument[7])))*100
        Wc2 = ((float(argument[2])-float(argument[4]))/(float(argument[6])-float(argument[6])))*100
        Wp = (Wc1+Wc2)/2

        Ip = Wl-Wp

        #flow index
        #import math
        W1 = (float(argument[1])+float(argument[3]))/2
        W2 = (float(argument[2])+float(argument[4]))/2
        If =(W2-W1)/(math.log10(float(argument[1])/float(argument[2])))

        #toughness index
        It = If/Ip


        print(json.dumps({"Test":[{"The toughness index of Liquid and plastic limit final is" : str(It)}]}))
        
    def Direct_shear_test(self):
        argument = self.arg[0:]
        AC1 = float(argument[0])*((30-float(argument[1]))/30)
        AC2 = float(argument[1])*((30-float(argument[2]))/30)
        AC3 = float(argument[2])*((30-float(argument[3]))/30)
        AC4 = float(argument[3])*((30-float(argument[4]))/30)
        AC5 = float(argument[4])*((30-float(argument[4]))/30)
        AC6 = float(argument[5])*((30-float(argument[5]))/30)
        AC7 = float(argument[5])*((30-float(argument[6]))/30)
        AC8 = float(argument[6])*((30-float(argument[7]))/30)
        AC9 = float(argument[7])*((30-float(argument[8]))/30)
        AC10 = float(argument[8])*((30-float(argument[9]))/30)
        AC11 = float(argument[9])*((30-float(argument[0]))/30)
        AC12 = float(argument[0])*((30-float(argument[1]))/30)
        AC13 = float(argument[1])*((30-float(argument[2]))/30)
        AC14 = float(argument[2])*((30-float(argument[3]))/30)
        AC15 = float(argument[3])*((30-float(argument[4]))/30)
        AC16 = float(argument[4])*((30-float(argument[5]))/30)
        AC17 = float(argument[5])*((30-float(argument[6]))/30)
        AC18 = float(argument[6])*((30-float(argument[7]))/30)
        AC19 = float(argument[7])*((30-float(argument[8]))/30)

            #stress
        S1 = float(argument[0])/float(argument[1])
        S2 = float(argument[1])/float(argument[2])
        S3 = float(argument[2])/float(argument[3])
        S4 = float(argument[3])/float(argument[4])
        S5 = float(argument[4])/float(argument[4])
        S6 = float(argument[5])/float(argument[5])
        S7 = float(argument[6])/float(argument[6])
        S8 = float(argument[7])/float(argument[6])
        S9 = float(argument[8])/float(argument[7])
        S10 = float(argument[8])/float(argument[8])
        S11 = float(argument[9])/float(argument[9])
        S12 = float(argument[0])/float(argument[0])
        S13 = float(argument[1])/float(argument[1])
        S14 = float(argument[2])/float(argument[2])
        S15 = float(argument[3])/float(argument[3])
        S16 = float(argument[4])/float(argument[4])
        S17 = float(argument[5])/float(argument[5])
        S18 = float(argument[5])/float(argument[6])
        S19 = float(argument[6])/float(argument[7])

        ls1 = float(argument[0])/float(argument[7])
        ls2 = float(argument[1])/float(argument[8])
        ls3 = float(argument[2])/float(argument[9])
        ls4 = float(argument[3])/float(argument[1])
        ls5 = float(argument[4])/float(argument[2])
        ls6 = float(argument[5])/float(argument[3])
        ls7 = float(argument[5])/float(argument[4])
        ls8 = float(argument[6])/float(argument[5])
        ls = (ls1 + ls2 + ls3 + ls4 + ls5 + ls6 + ls7 + ls8)/8 


        print(json.dumps({"Test":[{"The Direct shear test output is" : str(ls)}]}))

        
        
    def Determination_of_shrinkage_limit(self):
        argument = self.arg[0:]

        #Volume of wet soil pat
        v1 = float(argument[1])/13.6
        v2 = float(argument[2])/13.6

        #Shrinkage limit
        Ws1 = (float(argument[1])-(((v1-float(argument[2]))/float(argument[3]))*100))

        Ws2 = (float(argument[3])-(((v2-float(argument[4]))/float(argument[5]))*100))

        Ws = (Ws1+Ws2)/2

            #shrinkage ratio
        wd = (float(argument[1])+float(argument[2]))/2
        Sr = wd/(float(argument[3])*float(argument[4]))

        #volumetric shrinkage
        Vs = (float(argument[1])-Ws)*Sr
        
        print(json.dumps({"Test":[{"The volumetric shrinkage output is" : str(Vs)}]}))
        
        
    def Specific_Gravity(self):
        argument = self.arg[0:]

        #Specific gravity of CG soil
        CGs = ((float(argument[0])-float(argument[1]))*float(argument[2]))/((float(argument[3])-float(argument[4]))-(float(argument[5])-float(argument[6])))

        #Specific gravity of CG soil
        FGs = ((float(argument[7])-float(argument[8]))*float(argument[9]))/((float(argument[10])-float(argument[11]))-(float(argument[12])-float(argument[13])))

        print(json.dumps({"Soil":[{"The Specific gravity of CG soil is" : str(FGs)}]}))
        
        
    def Determination_of_free_swell_index(self):
        argument = self.arg[0:]

        #free swell Index
        FSI = ((float(argument[1])-float(argument[3]))/float(argument[2]))*100


        print(json.dumps({"Test":[{"The free swell Index is" : str(FSI)}]}))

        
    def Standard_proctor(self):
        argument = self.arg[0:]
        A=float(argument[1])
        B=float(argument[2])
        print(json.dumps({"Test":[{"The maximum dry density of the given soil sample is":str(A),"The optimum moisture content is":str(B)}]}))
   

 
    def Triaxial_Shear_test(self):
        argument = self.arg[0:]

        #strain
        E1 = (float(argument[1])/float(argument[1]))
        E2 = (float(argument[2])/float(argument[2]))
        E3 = (float(argument[3])/float(argument[3]))
        E4 = (float(argument[4])/float(argument[4]))
        E5 = (float(argument[5])/float(argument[5]))
        E6 = (float(argument[6])/float(argument[5]))
        E7 = (float(argument[7])/float(argument[6]))
        E8 = (float(argument[8])/float(argument[6]))
        E9 = (float(argument[9])/float(argument[7]))
        E10 = (float(argument[0])/float(argument[8]))
        E11 = (float(argument[1])/float(argument[9]))
        E12 = (float(argument[2])/float(argument[0]))
        E13 = (float(argument[3])/float(argument[1]))
        E14 = (float(argument[4])/float(argument[2]))
        E15 = (float(argument[5])/float(argument[3]))
        E16 = (float(argument[6])/float(argument[4]))
        E17 = (float(argument[7])/float(argument[5]))
        E18 = (float(argument[8])/float(argument[6]))

        AC1 = (float(argument[1])/(1-E1))
        AC2 = (float(argument[2])/(1-E2))
        AC3 = (float(argument[3])/(1-E3))
        AC4 = (float(argument[4])/(1-E4))
        AC5 = (float(argument[5])/(1-E5))
        AC6 = (float(argument[6])/(1-E6))
        AC7 = (float(argument[6])/(1-E7))
        AC8 = (float(argument[7])/(1-E8))
        AC9 = (float(argument[8])/(1-E9))
        AC10 = (float(argument[9])/(1-E10))
        AC11 = (float(argument[0])/(1-E11))
        AC12 = (float(argument[1])/(1-E12))
        AC13 = (float(argument[2])/(1-E13))
        AC14 = (float(argument[3])/(1-E14))
        AC15 = (float(argument[4])/(1-E15))
        AC16 = (float(argument[6])/(1-E16))
        AC17 = (float(argument[7])/(1-E17))
        AC18 = (float(argument[8])/(1-E18))

        #stress
        S1 = float(argument[0])/float(argument[0])
        S2 = float(argument[1])/float(argument[1])
        S3 = float(argument[2])/float(argument[2])
        S4 = float(argument[3])/float(argument[3])
        S5 = float(argument[4])/float(argument[4])
        S6 = float(argument[5])/float(argument[5])
        S7 = float(argument[5])/float(argument[6])
        S8 = float(argument[6])/float(argument[6])
        S9 = float(argument[7])/float(argument[7])
        S10 = float(argument[8])/float(argument[7])
        S11 = float(argument[9])/float(argument[4])
        S12 = float(argument[0])/float(argument[2])
        S13 = float(argument[1])/float(argument[4])
        S14 = float(argument[2])/float(argument[1])
        S15 = float(argument[3])/float(argument[2])
        S16 = float(argument[4])/float(argument[4])
        S17 = float(argument[5])/float(argument[5])
        S18 = float(argument[6])/float(argument[6])

        #strain
        e1 = (float(argument[0])/float(argument[0]))
        e2 = (float(argument[1])/float(argument[1]))
        e3 = (float(argument[2])/float(argument[2]))
        e4 = (float(argument[3])/float(argument[3]))
        e5 = (float(argument[4])/float(argument[4]))
        e6 = (float(argument[5])/float(argument[4]))
        e7 = (float(argument[6])/float(argument[5]))
        e8 = (float(argument[7])/float(argument[6]))
        e9 = (float(argument[8])/float(argument[1]))
        e10 = (float(argument[9])/float(argument[3]))
        e11 = (float(argument[0])/float(argument[3]))
        e12 = (float(argument[1])/float(argument[4]))
        e13 = (float(argument[2])/float(argument[4]))
        e14 = (float(argument[3])/float(argument[5]))
        e15 = (float(argument[4])/float(argument[6]))
        e16 = (float(argument[5])/float(argument[1]))
        e17 = (float(argument[6])/float(argument[4]))
        e18 = (float(argument[1])/float(argument[5]))
        e19 = (float(argument[2])/float(argument[1]))
        e20 = (float(argument[2])/float(argument[5]))
        e21 = (float(argument[5])/float(argument[5]))

        S1 = float(argument[0])/float(argument[1])
        S2 = float(argument[2])/float(argument[2])
        S3 = float(argument[3])/float(argument[3])
        S4 = float(argument[4])/float(argument[3])
        S5 = float(argument[5])/float(argument[4])
        S6 = float(argument[6])/float(argument[5])
        S7 = float(argument[7])/float(argument[6])
        S8 = float(argument[7])/float(argument[7])
        S9 = float(argument[8])/float(argument[7])
        S10 = float(argument[8])/float(argument[1])
        S11 = float(argument[9])/float(argument[2])
        S12 = float(argument[0])/float(argument[4])
        S13 = float(argument[1])/float(argument[0])
        S14 = float(argument[2])/float(argument[1])
        S15 = float(argument[3])/float(argument[3])
        S16 = float(argument[4])/float(argument[2])
        S17 = float(argument[5])/float(argument[4])
        S18 = float(argument[6])/float(argument[5])
        s19 = float(argument[6])/float(argument[6])
        s20 = float(argument[7])/float(argument[7])
        s21 = float(argument[9])/float(argument[7])

        gama1 = float(argument[0])+float(argument[2])
        gama2 = float(argument[1])+float(argument[3])
        ratio1 = gama1/float(argument[4])
        ratio2 = gama2/float(argument[5])

        print(json.dumps({"Test":[{"The ratio of Triaxial Shear test is" : str(ratio1),"and":str(ratio2)}]}))        
        # print(json.dumps({"Test":[{"The ratio of Triaxial Shear test  is" : str(ratio2)}]}))

