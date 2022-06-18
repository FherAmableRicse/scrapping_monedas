import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = requests.get("https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx")

def grabarMonedas(monedas):
    strMonedas = ""
    for l in monedas:
        for clave,valor in l.items():
            strMonedas += valor
            if clave != 'venta':
                strMonedas += ';'
            else:
                strMonedas += '\n'
    return strMonedas

def scrapping_tipocambio():
    try:
        (url.status_code == 200)
        print("pagina encontrada")
        html = BeautifulSoup(url.text,'html.parser')
        listaMonedas = []
        for i in range(7):
            fila = html.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__' + str(i)})
            moneda = fila.find('td',{'class':'APLI_fila3'})
            compra = fila.find('td',{'class':'APLI_fila2'})
            venta = fila.find('td',{'class':'APLI_fila2'}).findNext('td') 
            dictMoneda = {
                'moneda': moneda.get_text(),
                'compra': compra.get_text(),
                'venta': venta.get_text()
            }
            listaMonedas.append(dictMoneda)

        columnas = ["Moneda","Compra","Venta"]
        tablaMonedas = [moneda.values() for moneda in listaMonedas]
        print(tabulate(tablaMonedas, headers=columnas,tablefmt="grid"))
        strMonedas = grabarMonedas(listaMonedas)
        fw = open('monedas.csv','w')
        fw.write(strMonedas)
        fw.close()
      
    except:
     print("error " + str(url.status_code))

    return listaMonedas
