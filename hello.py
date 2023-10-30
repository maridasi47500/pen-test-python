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
  def bluetooth(self,myscript):
    print("myscript", myscript)
    self.figure.set_content(Fichier("./welcome","appareilbluetooth.html").lire())
    self.set_path("./monscript")
    self.set_file("mesairpods.sh")
    self.set_runthisprogram(run=True)
    return self

  def variable(self,myscript):
    print("myscript", myscript)
    self.figure.set_content(Fichier("./welcome","appareilbluetooth.html").lire())
    self.set_path("./monscript")
    self.set_file("variables.sh")
    self.set_runthisprogram(run=True)
    return self
  def hautparleurjack(self,myscript):
    print("myscript", myscript)
    self.figure.set_content(Fichier("./welcome","hautparleurjack.html").lire())
    self.set_path("./monscript")
    self.set_file("hautparleurjack.sh")
    self.set_runthisprogram(run=True)
    return self
  def hautparleur(self,myscript):
    print("myscript", myscript)
    self.figure.set_content(Fichier("./welcome","appareilbluetooth.html").lire())
    self.set_path("./monscript")
    self.set_file("monhautparleur.py")
    self.set_runthisprogram(run=True)
    return self
  def airpods(self,myscript):
    print("myscript", myscript)
    self.figure.set_content(Fichier("./welcome","appareilbluetooth.html").lire())
    self.set_path("./monscript")
    self.set_file("bluetooth.py")
    self.set_runthisprogram(run=True)
    return self
