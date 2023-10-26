import re
from hello import Hello
from erreur import Erreur
from render import Render
from mybing import Bing
from traduction import Traduction


class Route():
  def __init__(self):
    self.params={}
    self.route={
r"/$":"Hello#hi",
r"/bienvenue$":"Hello#hi",
r"/bluetooth$":"Hello#bluetooth",
r"/variables$":"Hello#variable",
r"/airpods$":"Hello#airpods",
r"/bing$":"Bing#search",
r"/traduire$":"Traduction#traduire",

}
  def get_route(self,myroute,myparams):
    print(myroute,myparams)
    print("myroute")
    self.params=myparams
    for i in self.route:
      j=self.route[i]
      if re.match(myroute, i):
        print(j, "my func found")
        loc = {}
        print("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"').work(params=params).encode()".format(params=myparams))
        exec("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"').work(params={params}).encode()".format(params=myparams),globals(),loc)
        print(loc["myvar"])
        print("loc")
        return loc["myvar"]
    mytext=(Erreur().err404().encode())
    return mytext
