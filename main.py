from flask import Flask
from bs4 import BeautifulSoup
import requests

application = Flask(__name__)

URL_COTIZACION_ORO_BCRA = "https://www.bcra.gob.ar/PublicacionesEstadisticas/Cotizacion_argentino_oro.asp"

@application.route("/")
def hello():
    page = requests.get(URL_COTIZACION_ORO_BCRA)
    soup = BeautifulSoup(page.content, 'html.parser')
    tabla = soup.find("div", {"class": "clearfix pagina-interior"})
    return str(tabla)

if __name__ == "__main__":
    application.run()
