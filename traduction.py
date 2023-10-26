import re
from render import Render
from fichier import Fichier
from translate import Translator
from bing import Bing as bing
import subprocess
import urllib
class Traduction():
  def __init__(self,path):
    self.path=path
    self.title="traduire de l'anglais"
    self.figure=Render(self.title)
    self.results=Render(self.title)
  def traduire(self,params):
    self.figure.set_content(Fichier("./welcome","index.html").lire())

    text=params["text"][0]
    lang=params["lang"][0]
    print("en uellelangue",lang)
    translator= Translator(to_lang=lang)
    translation = translator.translate(text+'('+lang+")")
    
    self.figure.set_my_params("maphrase",text)
    self.figure.set_my_params("traduction",translation)

    self.figure.ajouter_a_mes_mots(Fichier("./welcome","traduire.html").lire())
    return self.figure.render_figure()
  def work(self,params):
      FUNCS={"traduire":self.traduire}
      print(self.path)
      for x in FUNCS:
        print(x)

        if x == self.path:
          y=FUNCS[x]
          print(y)
          return y(params)
