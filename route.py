import re
from hello import Hello
from erreur import Erreur
from render import Render
from mybing import Bing
from traduction import Traduction
from mypic import Pic
from music import Music
from javascript import Js


class Route():
  def __init__(self):
    self.params={}
    self.route={
r"/$":"Hello#hi",
r"/bienvenue$":"Hello#hi",
r"/bluetooth$":"Hello#bluetooth",
r"/cartedispo$":"Hello#cartedispo",
r"/cartedisporeset$":"Hello#cartedisporeset",
r"/test$":"Hello#test",
r"/hautparleur$":"Hello#hautparleur",
r"/tether$":"Hello#tether",
r"/maradio$":"Hello#maradio",
r"/monhautparleurjack$":"Hello#hautparleurjack",
r"/variables$":"Hello#variable",
r"/airpods$":"Hello#airpods",
r"/bing$":"Bing#search",
r"/recording$":"Music#recording",
r"/traduit$":"Traduction#traduit",
r"/music$":"Music#music",
r"/traduire$":"Traduction#traduire",

}
  def get_route(self,myroute,myparams,mydata):
    print(myroute,myparams)
    print("myroute")

    self.params=myparams
    if myroute.endswith("ico"):
        myProgram=Pic(myroute)
        return myProgram
    elif myroute.endswith(".js"):
        myProgram=Js(name=myroute)
        return myProgram
    else:
        for i in self.route:
          j=self.route[i]
          if re.match(i,myroute):
            print(j, "my func found")
            loc = {}
            print("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"').work(params=params).encode()".format(params=myparams))
            exec("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"')",globals(),loc)
            print(loc["myvar"])
            print("loc")
            if mydata:
                exec("myvar=mydata(myProgram=myvar)",globals(), loc)
            exec("myvar=myvar.work(params={params})".format(params=myparams),globals(),loc)
            return loc["myvar"]
        mytext=(Erreur().err404())
        return mytext
