class Fichier:
  def __init__(self,path,name):
    self.path=path
    self.name=name
  def lire(self):
    j=open(self.path+"/"+self.name, "r")
    return j.read()
