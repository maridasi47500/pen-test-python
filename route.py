import re
from hello import Hello
from erreur import Erreur
from render import Render
from mybing import Bing
from traduction import Traduction
from mypic import Pic
from music import Music
from son import Son
from javascript import Js


class Route():
  def __init__(self):
    self.params={}
    self.route={
r"/$":"Hello#hi",
r"/bienvenue$":"Hello#hi",
r"/bluetooth$":"Hello#bluetooth",
r"/hautparleur$":"Hello#hautparleur",
r"/tether$":"Hello#tether",
r"/maradio$":"Hello#maradio",
r"/monhautparleurjack$":"Hello#hautparleurjack",
r"/variables$":"Hello#variable",
r"/airpods$":"Hello#airpods",
r"/bing$":"Bing#search",
r"/recording$":"Music#recording",
r"/tuner$":"Music#tuner",
r"/tunerinstrument$":"Music#tunerinstrument",
r"/mymusic$":"Music#normalizeaudio",
r"/traduit$":"Traduction#traduit",
r"/music$":"Music#music",
r"/allmymusic$":"Music#allmymusic",
r"/traduire$":"Traduction#traduire",
r"/changetone$":"Music#step1",
r"/mytone$":"Music#mytone",
r"/pluslent$":"Music#pluslent",
r"/pluslent$":"Music#pluslent",
r"/showmusic/([\d\-]+)":"Music#showmusic",

}
  def get_route(self,myroute,myparams,mydata=None):
    print(myroute,myparams)
    print("myroute")

    self.params=myparams
    if myroute.endswith("ico"):
        myProgram=Pic(myroute)
        return myProgram
    elif myroute.endswith(".wav"):
        myProgram=Son(name=myroute)
        return myProgram
    elif myroute.endswith(".js"):
        myProgram=Js(name=myroute)
        return myProgram
    else:
        for i in self.route:
          j=self.route[i]
          m = re.match(myroute,i)
          if m:

            groups= m.groups()
            params["groupsparams"]=groups

            print(j, "my func found")
            loc = {}
            print("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"').work(params=params).encode()".format(params=myparams))
            exec("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"')",globals(),loc)
            print(loc["myvar"])
            print("=my var")
            print(mydata)
            print("=my data")
            loc["myparams"]=myparams
            #loc["mydata"]=None


            if mydata:

                loc["myvar"].set_mydata(mydata)
                loc["mydata"]=mydata
                exec("myvar.set_mydata(mydata)",globals(),loc)
                print("=mydata")

            exec("myvar=myvar.work(params=myparams)",globals(),loc)

            return loc["myvar"]
        mytext=(Erreur().err404())
        return mytext
