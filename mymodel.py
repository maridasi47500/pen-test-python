class Mymodel():
    def __init__(self,params):
        for x in params:
            loc={"self": self,"params": params,"y":x}
            exec("self.set_"+x+"(params[y])",globals(),loc)

