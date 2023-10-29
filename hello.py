import re
from render import Render
from fichier import Fichier
import subprocess
from myfunc import Myfunc
class Hello(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="aide informatique"
    self.figure=Render(self.title)
  def get_figure(self):
    return self.figure
  def hi(self,myscrit):
    print("hi there &")
    self.figure.set_content(Fichier("./welcome","index.html").lire())
    print("hi there")
    return self
  #def work(self,params):
  #  FUNCS={"hi":self.hi,"bluetooth":self.bluetooth,'hautparleurjack':self.hautparleurjack,'hautparleur':self.hautparleur, "variable":self.variable, "airpods": self.airpods}
  #  MYPROGRAM={"hi": [],'hautparleurjack':['hdajackretask'],"bluetooth":['sh',"./monscript/mesairpods.sh"], "variable":['sh',"./monscript/variables.sh"], "hautparleur": ['python3',"./monscript/monhautparleur.py"], "airpods": ['python3',"./monscript/bluetooth.py"]}
  #  print(self.path)
  #  for x in FUNCS:
  #    print(x)

  #    if x == self.path:
  #      y=FUNCS[x]
  #      print(y)
  #      return y(MYPROGRAM[x])
  def bluetooth(self,myscript):

    try:
      x = subprocess.check_output(myscript)
    except Exception as e:
      x = "il y a eu une erreur"+str(e)
    
    if b"Restarting bluetooth" in x:
      self.figure.set_content(str(x)+"ok le bluetooth a été reinitialise")
    else:
      self.figure.set_content(str(x)+"le bluetooth n'a pas bien été reinitialise. relancer le script")
    return self
  def variable(self,myscript):
    try:
      x = subprocess.check_output(myscript)
    except Exception as e:
      x = "il y a eu une erreur"+str(e)
    if b"arrivee" in x and b" la fin" in x:
      self.figure.set_content(str(x)+"ok les variables ont ete initialisee")
    else:
      self.figure.set_content(str(x)+"oh no les variables n'ont pas ete initialisee")
    return self
  def hautparleurjack(self,myscript):
    try:
      x = subprocess.check_output(myscript)
      print(x, type(x).__name__,"myu haut aprleyr")
      
      if type(x) is bytes:
          x="ok le haut parleur a été branché en jack"
    except Exception as e:
      x = "il y a eu une erreur"+str(e)
    self.figure.set_content(x)
    return self
  def hautparleur(self,myscript):
    try:
      x = subprocess.check_output(myscript)
    except Exception as e:
      x = "il y a eu une erreur"+str(e)
    self.figure.set_content(x)
    return self
  def airpods(self,myscript):
    try:
      x = subprocess.check_output(myscript)
    except Exception as e:
      x = "il y a eu une erreur"+str(e)
    self.figure.set_content(x)
    return self
