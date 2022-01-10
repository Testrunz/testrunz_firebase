import json
class Dummy:
  def __init__(self, arg):
        self.arg = arg
  def dummy(self):
        argument = self.arg[0:]
        dumArg =  (argument[1])
        print(json.dumps({"result":[{"output" : str(dumArg) }]}))
       