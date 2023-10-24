import re
from hello import Hello
from erreur import Erreur
from render import Render


class Route():
  def __init__(self):
    self.route={
"/$":"Hello#hi",
"/bluetooth$":"Hello#bluetooth",
"/variables$":"Hello#variable",
"/airpods$":"Hello#airpods",

}
  def get_route(self,myroute):
    print(myroute)
    print("myroute")
    for i in self.route:
      j=self.route[i]
      if re.match(myroute, i):
        loc = {}
        print("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"').work().encode()")
        exec("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"').work().encode()",globals(),loc)
        print(loc["myvar"])
        print("loc")
        return loc["myvar"]
    mytext=(Erreur().err404().encode())
    return mytext
