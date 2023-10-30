import re
from render import Render
from fichier import Fichier
import subprocess
import urllib
from myfunc import Myfunc
class Music(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="aide informatique"
    self.figure=Render(self.title)
    self.results=Render(self.title)
    self.upload=False
  def music(self,params):
    self.figure.set_content(Fichier("./music","_form.html").lire())

    self.figure.ajouter_a_mes_mots("sauver cet enregistrement dans cette page puis voir le morceau")
    return self
  def recording(self,params):
    print(params, "params recording")
    self.set_uploads(["recording"])
    print(self.get_upload(), "upload...")
    self.figure.set_content(Fichier("./welcome","index.html").lire())

    self.figure.ajouter_a_mes_mots(Fichier("./music","music.html").lire())

    return self


