class Render():
  def __init__(self,title):
    self.title=title
    self.body=title
    self.headingone=title
  def get_title(self):
    return self.title
  def get_headingone(self):
    return self.title
  def get_body(self):
    return self.body
  def set_content(self,mybody):
    self.body=mybody
  def ajouteramesmots(self,mot):
    self.body += mot
  def render_figure(self):
    return """<html>

<head>
<title>{debutdemesmots}</title>
</head>
<body>
<nav><div>à la racine tu as un fichir ./venv/bin/activate avec ecrit dedans 'export MESAIRPODS="mac adresse de mes airpods"'(1) </div><a href="/bluetooth">je n'arrive pas à connecer mes appareils blueooth (reinitaliser bluetooth ) (2)</a>
<a href="/airpods">mes airpods sont pas connectes (3)</a>
<a href="/">welcome</a></nav>
<h1>{mots}</h1>
{partiedemesmot}
</body>
</html>""".format(mots=self.get_headingone(),debutdemesmots=self.get_title(),partiedemesmot=self.get_body())
