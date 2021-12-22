import json

class com3:
    def __init__(self, arg):
        self.arg = arg
        
    def GUNN_DIODE(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Gunn Diode Characteristics is completed sucessfully"}]}))

        
    def REFLEX_KLYSTRON(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Mode Characteristics of Reflex Klystron is completed sucessfully"}]}))
        
    def ISOLATOR_CIRCULATOR(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Characteristics of Circulator and Isolator is completed sucessfully"}]}))
        
        
    def EPLANE_AND_HIPLANE_TEE(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Characteristics of E-Plane and H-Plane Tee is completed sucessfully"}]}))
        
        
    def MAGIC_TEE(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Characteristics of Magic Tee is completed sucessfully"}]}))
        
        
    def DIRECTIONAL_COUPLER(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Characteristics of Directional Coupler is completed sucessfully"}]}))
        
        
    def HORN_ANTENNA(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Radiation Pattern of Horn Antenna completed sucessfully"}]}))
        
        
    def MEASUREMENT_OF_IMPEDANCE(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Measurement of impedance is completed sucessfully"}]}))

    def FIBRE_OPTIC_MEASUREMENTS(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Fiber Optics Measurement is completed sucessfully"}]}))
        
        
    def FIBRE_OPTIC_LED(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Characteristics of LED completed sucessfully"}]}))
        
        
    def APD(self):
        argument = self.arg[0:]
        print(json.dumps({"Software":[{"Result":"The Characteristics of APD is completed sucessfully"}]}))

 