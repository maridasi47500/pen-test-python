
from __future__ import division
import re
from render import Render
from fichier import Fichier
import subprocess
import urllib
from myfunc import Myfunc
from db import Db
from myrecording import Myrecording


#import numpy as np
#from scipy.io.wavfile import write
class Music(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="aide informatique"
    self.figure=Render(self.title)
    self.results=Render(self.title)
    self.upload=False
    self.recparams=["filename", "artist","title","tonalite"]
  def tunerinstrument(self,params):
    self.figure.set_content(Fichier("./music","tuner.html").lire())

    self.figure.ajouter_a_mes_mots("sauver cet enregistrement dans cette page puis voir le morceau")
    instrument= params["instrument"][0]
    self.figure.set_my_params("note", "toutes les notes")
    self.figure.set_my_params("instrument", params["instrument"][0])
    notes=Db().get_notes_instrument(instrument)
    print(notes)
    self.figure.set_my_params("notes", notes)



    return self
  def tuner(self,params):
    self.figure.set_content(Fichier("./music","tuner.html").lire())

    self.figure.ajouter_a_mes_mots("sauver cet enregistrement dans cette page puis voir le morceau")
    note= params["note"][0]
    instrument= params["instrument"][0]
    self.figure.set_my_params("note", params["note"][0])
    self.figure.set_my_params("instrument", params["instrument"][0])
    notes=Db().get_notes(params["instrument"][0], params["note"][0])
    self.figure.set_my_params("notes", notes)

    rate = 44100  # Sampling rate [samples/s].
    n = 44100     # Length [samples].
    f = 1000      # Frequency of the sine [Hz].
    t = np.linspace(0, n / rate, n, endpoint=False)
    
    f=float(notes[0]["frequency"])
    note1 = np.sin(2 * np.pi * f * t)
    do=np.round(note1 * 32767).astype(np.int16)
    write('./uploads/{instrument}_{note}.wav'.format(instrument=instrument, note=note), rate, do)


    return self
  def showmusic(self,params):
    self.set_my_list_params(["id"])
    self.set_my_params(self.groupsparams)
    self.figure.set_content(Fichier("./music","show.html").lire())

    self.figure.ajouter_a_mes_mots("page web d'1 enregistrements musique")
    return self
  def allmymusic(self,params):
    self.figure.set_content(Fichier("./music","all.html").lire())

    self.figure.ajouter_a_mes_mots("page web des enregistrements musique")
    return self
  def music(self,params):
    self.figure.set_content(Fichier("./music","_form.html").lire())

    self.figure.ajouter_a_mes_mots("sauver cet enregistrement dans cette page puis voir le morceau")
    return self
  def recording(self,params):
    print(params, "params recording")
    somedata=self.get_mydata()(self.recparams)

    rec=Myrecording(somedata).mynew()
    if rec:
      print("uploaded and save...")
    self.figure.set_content(Fichier("./welcome","index.html").lire())


    return self
  def normalizeaudio(self,myscript):
    print("myscript", myscript)
    self.figure.set_content(Fichier("./welcome","appareilbluetooth.html").lire())
    self.set_myargs(["normalize-audio","-m",myscript["mymusic"][0]+"/*"])
    self.set_runthisprogram(run=True)
    return self



