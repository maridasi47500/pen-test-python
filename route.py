import re
from hello import Hello
from erreur import Erreur
from render import Render
from mygoogle import Google


class Route():
  def __init__(self):
    self.params={}
    self.route={
"/$":"Hello#hi",
"/bluetooth$":"Hello#bluetooth",
"/variables$":"Hello#variable",
"/airpods$":"Hello#airpods",
"/google$":"Google#search",

}
  def get_route(self,myroute,myparams):
    print(myroute,myparams)
    print("myroute")
    self.params=myparams
    for i in self.route:
      j=self.route[i]
      if re.match(myroute, i):
        loc = {}
        print("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"').work(params=params).encode()".format(params=myparams))
        exec("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"').work(params={params}).encode()".format(params=myparams),globals(),loc)
        print(loc["myvar"])
        print("loc")
        return loc["myvar"]
    mytext=(Erreur().err404().encode())
    return mytext
