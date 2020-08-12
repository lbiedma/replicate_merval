from bs4 import BeautifulSoup
from urllib import request
import ssl

def get_rfx20_comp():
    """
    Función para obtener un DataFrame con la composición de la cartera actual del
    RFX20, desde su página web. Si no se cae ni cambian la página, debería funcionar bien.
    """
    url = "http://www.rofex.com.ar/cem/CarteraVigenteROFEX20"
    gcontext = ssl.SSLContext()  # Only for gangstars
    soup = BeautifulSoup(request.urlopen(url, context=gcontext))

    table = soup.find("table", attrs={"id":"ctl00_ContentPlaceHolder1_tblCotizacionIndice"})
    l = []
    for tr in table.find_all("tr")[2:-3]:
        td = tr.find_all('td')
        row = [tr.text.strip().replace(",", ".") for tr in td]
        l.append(row)
    cartera = pd.DataFrame(l, columns=["Accion", "Cantidad"])
    cartera["Cantidad"] = pd.to_numeric(cartera["Cantidad"])

    return cartera

