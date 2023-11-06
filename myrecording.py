from mymodel import Mymodel
from db import Db
class Myrecording(Mymodel):
    def set_filename(self,uploaded_io):
        if isinstance(uploaded_io, list):
            for record in uploaded_io:
                open("./uploads/%s"%record.filename, "wb").write(record.file.read())
        else:
            open("./uploads/%s"%uploaded_io.filename, "wb").write(uploaded_io.file.read())
        print("name")
        self.filename=uploaded_io.filename
    def get_filename(self):
        return self.recording
    def save(self):
        x=Db()
    def set_artist(self,string):
        self.artist=string
    def get_artist(self,string):
        return self.artist
    def set_title(self,string):
        self.title=string
    def get_title(self,string):
        return self.title
    def set_tonalite(self,string):
        self.tonalite=string
    def get_tonalite(self,string):
        return self.tonalite


