from render import Render
class Erreur():
  def __init__(self):
    self.route={"/":"Hello#hi"}
  def err404(self):
    myProgram=Render("erreur 404 non trouvé")
    return myProgram.render_figure()
