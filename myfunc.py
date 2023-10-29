from render import Render
class Myfunc():
    pic=False
    js=False
    figure=Render("hi") 
    upload=False
    def get_figure(self):
        return self.figure
    def get_pic(self):
        return self.pic
    def get_js(self):
        return self.js
    def set_upload(self,name):
        self.upload=name
    def get_upload(self):
        return self.upload
    def get_html(self):
        return self.get_figure().render_figure().encode()
    def run(self,params):
        print("frgthjk")
    def file(self,params):
        print("frgthjk")
    def run(self,params):
    def work(self,params):
        loc={"self":self, "params": params}
        exec("myvar=self.{myfunc}(params)".format(myfunc=self.path), globals(), loc)
        return loc["myvar"]

