import requests
import urllib.request
from bs4 import BeautifulSoup


def run():
    response = requests.get('https://www.loteriademedellin.com.co/', verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    numerosGanadores = soup.findAll("div", {"class": "ultimo_sorteo_ganador__digit"})
    print("-----------*----------------")
    # Descargamos los ultimos resultado de la loteria de medellin
    for item in numerosGanadores:
        print(item.find('div'))


if __name__ == '__main__':
    run()
