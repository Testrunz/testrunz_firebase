import json
import math
class Dom:
    def __init__(self, arg):
        self.arg = arg
    def Single_Helical(self):
        argument = self.arg[:]
#got output
        #print(argument)
        w1 = float(argument[4])*9.81
        w2 = float(argument[6])*9.81
        w3 = float(argument[8])*9.81
        w4 = float(argument[10])*9.81
        Avg =round((w1+w2+w3+w4)/4)
        S1 = w1/float(argument[5])
        S2 = w2/float(argument[7])
        S3 = w3/float(argument[9])
        S4 = w4/float(argument[11])
        S = round((S1+S2+S3+S4)/4)
        Ttheo1 = 2*math.pi*math.sqrt(w1/S)
        Ttheo2 = 2*math.pi*math.sqrt(w2/S)
        Ttheo3 = 2*math.pi*math.sqrt(w3/S)
        Ttheo4 = 2*math.pi*math.sqrt(w4/S)
        Theo = (Ttheo1+Ttheo2+Ttheo3+Ttheo4)/4
        Texp1 = float(argument[14])/float(argument[13])
        Texp2 = float(argument[17])/float(argument[16])
        Texp3 = float(argument[20])/float(argument[19])
        Texp4 = float(argument[23])/float(argument[22])
        Texp = round((Texp1+Texp2+Texp3+Texp4)/4)
        print(json.dumps({"Lee":[{"Weight" : str(Avg) + "N"}], "Vernier":[{"Stiffness" : str(S) + "N/m"}], "tickness":[{"Theoretical time period" : str(Theo)}], "Thermal":[{"Periodic time" : str(Texp) + "sec"}], "The":[{"Result":"Thus the frequency of vibration of the helical spring is determined successfully both experimentally and the required graph is drawn"}]}))
    def Torsional(self):
        argument = self.arg[:]
        Texp1 = float(argument[6])/float(argument[5])
        Texp2 = float(argument[9])/float(argument[8])
        Texp3 = float(argument[12])/float(argument[11])
        Texp4 = float(argument[15])/float(argument[14])
        Texp = round((Texp1+Texp2+Texp3+Texp4)/4)
        I = float(argument[3])*0.25**2/8
        Ip = math.pi*0.25**4/32
        K1 = 0.8*10**4*Ip/float(argument[16])
        K2 = 0.8*10**4*Ip/float(argument[17])
        K3 = 0.8*10**4*Ip/float(argument[18])
        K4 = 0.8*10**4*Ip/float(argument[19])
        K =(K1+K2+K3+K4)/4
        Ttheo1 = 2*math.pi*math.sqrt(I/K1)
        Ttheo2 = 2*math.pi*math.sqrt(I/K2)
        Ttheo3 = 2*math.pi*math.sqrt(I/K3)
        Ttheo4 = 2*math.pi*math.sqrt(I/K4)
        Ttheo = (Ttheo1+Ttheo2+Ttheo3+Ttheo4)/4
        Fnt =  round((1/Ttheo1)+(1/Ttheo2)+(1/Ttheo3)+(1/Ttheo4))/4
        Fne = round((1/Texp1)+(1/Texp2)+(1/Texp3)+(1/Texp4))/4
        error = (Fnt-Fne)/Fnt
        print(json.dumps({"Lee":[{"Torsional stiffness" : str(K) + "Nm"}], "Vernier":[{"Theoretical" : str(Ttheo)}], "tickness":[{"T experimental" : str(Texp)+"Sec"}], "Thermal":[{"Natural frequency" : str(Fnt) + "Hz"}], "Ther":[{"Percentage Error" : str(error) + "%"}], "The":[{"Result":"Thus the torsional vibration of single rotor shaft system is determined and the characteristic curve is drawn"}]}))
    def Two_Rotor(self):
        argument = self.arg[:]
        Ia1 = 2.8*(0.225**2/8)
        Ia2 = 2.8*(0.225**2/8)
        Ia3 = 2.8*(0.225**2/8)
        Ia4 = 2.8*(0.225**2/8)
        Ia =(Ia1+Ia2+Ia3+Ia4)/4
        Ib1 = 1.95*(0.19**2/8)
        Ib2 = 1.95*(0.19**2/8)
        Ib3 = 1.95*(0.19**2/8)
        Ib4 = 1.95*(0.19**2/8)
        Ib =(Ib1+Ib2+Ib3+Ib4)/4
        Texp1 = float(argument[4])/float(argument[3])
        Texp2 = float(argument[7])/float(argument[6])
        Texp3 = float(argument[10])/float(argument[9])
        Texp4 = float(argument[13])/float(argument[12])
        Texp = round((Texp1+Texp2+Texp3+Texp4)/4)
        Ip = math.pi*0.3**4/32
        K = 0.8*10**4*Ip/float(argument[1])
        Ttheo = math.sqrt(Ia*Ib/K*(Ia+Ib))
        Fnt = 1/Ttheo
        Fne = 1/Texp
        print(json.dumps({"Lee":[{"Mass moment of inertia Disc A" : str(Ia) + "Kgm2"}], "Ver":[{"Mass moment of inertia Disc B" : str(Ib) + "Kgm2"}], "tickness":[{"Time period" : str(Ttheo)}], "Thermal":[{"T experimental" : str(Texp)}], "Ther":[{"Natural frequency Fn the0" : str(Fnt)}],"Th":[{"Natural frequency Fn exp" : str(Fne)}], "The":[{"Result":"Thus the torsional vibration of two rotor system is studied and the natural frequency of vibration is determined both experimentally and theoretically"}]}))

    def Radius(self):
        argument = self.arg[:]
        OG1= float(argument[2])/2
        OG2= float(argument[5])/2
        OG3= float(argument[8])/2
        OG4= float(argument[11])/2
        Texp1 = float(argument[4])/float(argument[3])
        Texp2 = float(argument[7])/float(argument[6])
        Texp3 = float(argument[10])/float(argument[9])
        Texp4 = float(argument[13])/float(argument[12])
        Texp = round((Texp1+Texp2+Texp3+Texp4)/4)
        Kexp1 = 2*math.pi*math.sqrt(Texp1**2*9.81*OG1/4*math.pi**2)
        Kexp2 = 2*math.pi*math.sqrt(Texp2**2*9.81*OG2/4*math.pi**2)
        Kexp3 = 2*math.pi*math.sqrt(Texp3**2*9.81*OG3/4*math.pi**2)
        Kexp4 = 2*math.pi*math.sqrt(Texp4**2*9.81*OG4/4*math.pi**2)
        Kexp = (Kexp1+Kexp2+Kexp3+Kexp4)/4
        Ktheo1= float(argument[2])/2*math.sqrt(3)
        Ktheo2= float(argument[5])/2*math.sqrt(3)
        Ktheo3= float(argument[8])/2*math.sqrt(3)
        Ktheo4= float(argument[11])/2*math.sqrt(3)
        Ktheo = (Ktheo1+Ktheo2+Ktheo3+Ktheo4)/4
        print(json.dumps({"Lee":[{"Experimental Time Period" : str(Texp) + "Sec"}], "Vernier":[{"Radius of Gyration experimental" : str(Kexp)}]}))
    def Bifilar(self):
        argument = self.arg[:]
    
        Tm1 = (float(argument[4])+float(argument[5]))/2
        Tm2 = (float(argument[7])+float(argument[8]))/2
        Tm3 = (float(argument[10])+float(argument[11]))/2
        Tm4 = (float(argument[13])+float(argument[14]))/2
        Tm5 = (float(argument[16])+float(argument[17]))/2
        Tm6 = (float(argument[19])+float(argument[20]))/2
        Texp1 = Tm1/(float(argument[3]))
        Texp2 = Tm2/(float(argument[6]))
        Texp3 = Tm3/(float(argument[9]))
        Texp4 = Tm4/(float(argument[12]))
        Texp5 = Tm5/(float(argument[15]))
        Texp6 = Tm6/(float(argument[18]))
        Texp = (Texp1+Texp2+Texp3+Texp4+Texp5+Texp6)/6
        Kexp = (Texp/2*math.pi)*float(argument[2])*math.sqrt(9.81/float(argument[1]))
        Ktheo = (float(argument[1])/2*math.sqrt(3))
        E = ((Ktheo-Kexp)/Kexp)*100
        print(json.dumps({"Lee":[{"Experimental Time Period" : str(Texp) + "Sec"}], "Vernier":[{"Radius of Gyration experimental" : str(Kexp)}], "tickness":[{"Theoretical Radius of gyration" : str(Ktheo)}],"tick":[{"Percentage Error" : str(E)+"%"}], "The":[{"Result":"Thus the radius of gyration of given compound pendulum(rectangular bar) is determined using bifilar suspension setup"}]}))

    def Damping(self):
        argument = self.arg[:]
        Ip = math.pi*(3**4)/32
        K = 0.8*10**4*Ip/(float(argument[3]))
        I = 8.4*0.25**2/8
        T= 2*math.pi*math.sqrt(I/K)
        ctc = math.sqrt(4*I*K)
        n = 1
        S = (1/n)*math.log(float(argument[3])/float(argument[4]))
        Ct = S/math.sqrt(4*math.pi**2+S**2)
        print(json.dumps({"Lee":[{"Time Period" : str(T) + "Sec"}], "Vernier":[{"Logarithmic decrement" : str(S)}], "tickness":[{"Critical damping fctor" : str(ctc)}],"tick":[{"Damping Ratio" : str(Ct)}], "The":[{"Result":"Thus the damped torsional oscillation and the damping coefficient is determined experimentally and respective curves are drawn"}]}))
    def Equivalent(self):
        argument = self.arg[:]
        S = float(argument[3])/float(argument[4])
        print(json.dumps({"Lee":[{"Time Period" : str(S) + "Sec"}], "Vernier":[{"Result":"Thus the forced vibration of the beam damping setup was calculated as in the tabulation"}]}))
    def Watt(self):
        argument = self.arg[:]
        N = (float(argument[1])+float(argument[3])+float(argument[5]))/3
        h1 = (90-float(argument[2])/2)
        h2 =(90-float(argument[4])/2)
        h3 =(90-float(argument[6])/2)
        a1 = math.acos(h1/130)
        a2 = math.acos(h2/130)
        a3 = math.acos(h3/130)
        r1 = 0.050+130*math.sin(a1)
        r2 = 0.050+130*math.sin(a2)
        r3 = 0.050+130*math.sin(a3)
        W=2*math.pi*N/60
        m= 0.55*1.6
        F1= ((m*r1*W**2)+(m*r2*W**2)+(m*r3*W**2))/3
        print(json.dumps({"Lee":[{"Centrifugal Force" : str(F1) + "N"}], "Vernier":[{"Result":"Thus the characteristic curves of watt governor is obtained"}]}))
    def Porter(self):
        argument = self.arg[:]
        N = (float(argument[1])+float(argument[3])+float(argument[5]))/3
        h1 = (90-float(argument[2])/2)
        h2 =(90-float(argument[4])/2)
        h3 =(90-float(argument[6])/2)
        a1 = math.acos(h1/130)
        a2 = math.acos(h2/130)
        a3 = math.acos(h3/130)
        r1 = 0.050+130*math.sin(a1)
        r2 = 0.050+130*math.sin(a2)
        r3 = 0.050+130*math.sin(a3)
        W=2*math.pi*N/60
        m= 0.55*1.6
        F1= ((m*r1*W**2)+(m*r2*W**2)+(m*r3*W**2))/3
        print(json.dumps({"Lee":[{"Centrifugal Force" : str(F1) + "N"}], "Vernier":[{"Result":"Thus the characteristic curves of porter governor is obtained."}]}))
    def Proell(self):
        argument = self.arg[:]
        N = (float(argument[1])+float(argument[3])+float(argument[5]))/3
        h1 = (90-float(argument[2])/2)
        h2 =(90-float(argument[4])/2)
        h3 =(90-float(argument[6])/2)
        a1 = math.acos(h1/130)
        a2 = math.acos(h2/130)
        a3 = math.acos(h3/130)
        r1 = 0.050+130*math.sin(a1)
        r2 = 0.050+130*math.sin(a2)
        r3 = 0.050+130*math.sin(a3)
        W=2*math.pi*N/60
        m= 0.55*1.6
        F1= ((m*r1*W**2)+(m*r2*W**2)+(m*r3*W**2))/3
        print(json.dumps({"Lee":[{"Centrifugal Force" : str(F1) + "N"}], "Vernier":[{"Result":"Thus the characteristic curves of proell governor is obtained."}]}))
    def Hartnell(self):
        argument = self.arg[:]
        N = (float(argument[1])+float(argument[3])+float(argument[5]))/3
        r1 = 138+(75/115*float(argument[2]))
        r2 = 138+(75/115*float(argument[4]))
        r3 = 138+(75/115*float(argument[6]))
        W=2*math.pi*N/60
        m= 0.55*1.6
        F1= ((m*r1*W**2)+(m*r2*W**2)+(m*r3*W**2))/3
        print(json.dumps({"Lee":[{"Centrifugal Force" : str(F1) + "N"}], "Vernier":[{"Result":"Thus the characteristic curves of Hartnell governor is obtained."}]}))
    def Static(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the experimental on static and dynamic balancing of four different mass is performed and the position of counter balancing weights are calculated and verfied."}]}))

    def Whirling(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the study is done on the critical speed of the shaft."}]}))
    def Gyroscopic(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the gyroscopic couple relation(T = 1WWp) is verified through the given motorized gyroscope setup."}]}))
    def Journal(self):
        argument = self.arg[0:]
        print(json.dumps({"answer":[{"result":"Thus the pressure distributions are studied and graphs are plotted."}]}))
    def Cam(self):
        argument = self.arg[:]
        S = (float(argument[2])+float(argument[3])+float(argument[4]))/3
        print(json.dumps({"Lee":[{"Smean" : str(S)}], "Vernier":[{"Result":"Thus the displacement, velocity and acceleration diagram of the cam profile with roller follower is drawn."}]}))









    

