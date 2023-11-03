from mymodel import Mymodel
from db import Db
class Myrecording(Mymodel):
    def set_recording(self,uploaded_io):
        if isinstance(uploaded_io, list):
            for record in uploaded_io:
                open("./uploads/%s"%record.filename, "wb").write(record.file.read())
        else:
            open("./uploads/%s"%uploaded_io.filename, "wb").write(uploaded_io.file.read())
        print("name")
        self.recording=uploaded_io.filename
    def get_recording(self):
        return self.recording
    def save(self):
        x=Db()
    def set_name(self,string):
        self.name=string
    def get_name(self,string):
        return self.name


