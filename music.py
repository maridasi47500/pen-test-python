
from __future__ import division
import re
from render import Render
from fichier import Fichier
import subprocess
import urllib
from myfunc import Myfunc


import numpy as np
from scipy.io.wavfile import write
class Music(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="aide informatique"
    self.figure=Render(self.title)
    self.results=Render(self.title)
    self.upload=False
  def tuner(self,params):
    self.figure.set_content(Fichier("./music","_form.html").lire())

    self.figure.ajouter_a_mes_mots("sauver cet enregistrement dans cette page puis voir le morceau")
    self.figure.set_param("notes", Db().get_notes(params["instrument"][0], params["note"][0])
    rate = 44100  # Sampling rate [samples/s].
    n = 44100     # Length [samples].
    f = 1000      # Frequency of the sine [Hz].
    t = np.linspace(0, n / rate, n, endpoint=False)
    f= 261 #do
    note1 = np.sin(2 * np.pi * f * t)
    do=np.round(note1 * 32767).astype(np.int16)
    write('sine.wav', rate, do)


    return self
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


