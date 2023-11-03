class Myrecording():
    def __init__(self,params):
        self.name=""
        self.recording=""
    def set_recording(self,uploaded_io):
        self.recording=uploaded_io[filename]
    def get_recording(self):
        return self.recording
    def set_name(self,string):
        self.name=string
    def get_name(self,string):
        return self.name


