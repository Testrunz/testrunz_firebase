import sys, getopt, time
import json
from MECH import MECH

def main(argv):
    argument = ''
    usage = 'usage: script.py -f <sometext>'
    try:
        opts, args = getopt.getopt(argv,"hf:",["foo="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ("-f", "--foo"):
            argument = arg.split()
            try:
                if((argument[len(argument) -2] == "DS") and (argument[len(argument) -1] == "test")):
                    MECH(argument).DS_test()
                elif((argument[len(argument) -4] == "single") and (argument[len(argument) -3] == "phase") and (argument[len(argument) -2] == "induction") and (argument[len(argument) -1] == "motor")):
                    Mech(argument).single_phase_induction_motor()
                elif((argument[len(argument) -4] == "Three") and (argument[len(argument) -3] == "phase") and (argument[len(argument) -2] == "Two") and (argument[len(argument) -1] == "Wattmeter")):
                    MECH(argument).Three_Phase_Two_Wattmeter()
                elif((argument[len(argument) -2] == "SPEED") and (argument[len(argument) -1] == "CONTROL")):
                    MECH(argument).SPEED_CONTROL()
                elif((argument[len(argument) -3] == "Single") and (argument[len(argument) -3] == "Phase") and (argument[len(argument) -1] == "Transformer")):
                    MECH(argument).Single_Phase_Transformer()
                elif((argument[len(argument) -2] == "SWINBURNES") and (argument[len(argument) -1] == "TEST")):
                    MECH(argument).SWINBURNES_TEST()
                elif((argument[len(argument) -4] == "OS") and (argument[len(argument) -3] == "DC") and (argument[len(argument) -2] == "SHUNT") and (argument[len(argument) -1] == "MOTOR")):
                    MECH(argument).OS_DC_SHUNT_MOTOR()
                elif((argument[len(argument) -3] == "efficiency") and (argument[len(argument) -3] == "motor") and (argument[len(argument) -1] == "generator")):
                    MECH(argument).efficiency_motor_generator()
                elif((argument[len(argument) 4] == "Three") and (argument[len(argument) -3] == "PHASE") and (argument[len(argument) -2] == "SQUIRREL") and (argument[len(argument) -1] == "CAGE")):
                    MECH(argument).Three_PHASE_SQUIRREL_CAGE()

                    

            except ValueError:
                print(json.dumps({"error":"value added error"}))
            


if __name__ == "__main__":
    main(sys.argv[1:])
