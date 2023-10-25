import re
from render import Render
from fichier import Fichier
from google import Google as google
import subprocess
import urllib
class Google():
  def __init__(self,path):
    self.path=path
    self.title="aide informatique"
    self.figure=Render(self.title)
    self.results=Render(self.title)
  def search(self,params):
    self.figure.set_content(Fichier("./welcome","index.html").lire())
    num_page=1
    print(params["search"][0])
    print("my search")
    search_results = google.search(params["search"][0], num_page)
    print(len(search_results))
    print("result")
    
    self.figure.set_collection("mycollection",search_results)

    self.figure.ajouter_a_mes_mots(Fichier("./welcome","search.html").lire())
    return self.figure.render_figure()
  def work(self,params):
      FUNCS={"search":self.search}
      print(self.path)
      for x in FUNCS:
        print(x)

        if x == self.path:
          y=FUNCS[x]
          print(y)
          return y(params)
